from odoo import fields ,models


class newscategory(models.Model):
    _name='news.category'
    _description = 'news category'
    tittle=fields.Char('CategoryTittle' ,required=True)
    article_ids = fields.Many2many(
        'news.article',
        string='Articles')



