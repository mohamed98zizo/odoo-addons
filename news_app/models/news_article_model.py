from odoo import fields, models


class newsarticle(models.Model):
    _name = 'news.article'
    _description = 'article information'
    tittle = fields.Char('Article tittle', required=True)
    date = fields.Date('article date')
    body = fields.Html('body')
    summary = fields.Char('Summary')
    thumbnail = fields.Binary('thumbnail')
    author_ids = fields.Many2many('res.partner', string='author')
    tags_ids = fields.Many2many(
       'news.tags',
     string='tags' )
