from odoo import fields, models



class ResPartner(models.Model):
    _inherit = 'res.partner'
    article_ids = fields.Many2many(
        'news.article',
        string="articles")
    isauthor=fields.Boolean(string="isauthor")


