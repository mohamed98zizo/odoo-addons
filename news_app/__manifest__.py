{
    'name': 'News Application',
    'description': 'newspaper.',
    'author': 'mohamed abdelaziz ',
    'depends': ['base'],
    'application': True,
    'data': ['security/news_access_rules.xml',
             'security/ir.model.access.csv',
        'views/article_menu.xml',
        'views/article_view.xml',
        'views/res_partner_view.xml',
        'views/category_view.xml',
        'views/category_menu.xml',
        'views/tags_view.xml',
        'views/tags_menu.xml'

    ]
}
