# -*- coding: utf-8 -*-
{
    'name': "bug 管理",

    'summary': """
        用于软件开发过程中的bug 管理""",

    'description': """
        用于软件开发过程中的bug 管理
    """,

    'author': "Fish",
    'website': "http://www.fish.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '11.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/bugs.xml',
        'views/follower.xml',
         'views/bugs_template.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}