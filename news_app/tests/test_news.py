from odoo.tests.common import TransactionCase


class TestNews(TransactionCase):


    def setUp(self, *args, **kwargs):


        result = super(TestNews, self).setUp(*args, **kwargs)
        group = self.env.ref('news_app.news_group_rule', False)
        user_demo = self.env.ref('base.user_demo')
        self.env = self.env(user=user_demo)
        group.write({'users': [(4,user_demo.id)]})
        return result



    def test_article(self):
        record = self.env['news.article'].create({'tittle': 'elkema'})
        record.write({'body': 'ahlyy win'})
        self.assertEqual(record.tittle, 'elkema')
        self.assertEqual(record.body, '<p>ahlyy win</p>')
        print('article tmam')

    def test_Tags(self):
        record=self.env['news.tags'].create({'tag_title':'sport'})

        self.assertEqual(record.tag_title ,'sport')
        record.write({'tag_title ':'sport'})
        self.assertEqual(record.tag_title ,'sport')
        print(record.tag_title )


    def test_category(self):
        record=self.env['news.category'].create({'tittle':'elkema'})

        self.assertEqual(record.tittle ,'elkema')
        record.write({'tittle ':'elkema'})
        self.assertEqual(record.tittle,'elkema')
        print(record.tittle)

    def test_author(self):
        record=self.env['res.partner'].create({'name':'ahme'})
        self.assertEqual(record.name,'ahme')
        record.write({'isauthor' :  True})
        self.assertTrue(record.isauthor)
        print('author tmmam')


