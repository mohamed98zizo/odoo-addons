from odoo import fields, models


class NewsTags(models.Model):
    _name='news.tags'
    _description='Tag information'
    tag_title = fields.Char('Tag title')
    article_ids = fields.Many2many(
        'news.article',
        string='Articles')

