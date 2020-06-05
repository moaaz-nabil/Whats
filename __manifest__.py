# -*- coding: utf-8 -*-
{
    'name': "whats App Messege",

    'summary': """
        Send whats App Message easly To Your Contacts
        """,

    'description': """
        Send whats App Message easly To Your Contacts
    """,

    'author': "Moaz Nabil",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'wizard/wizard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable' : True ,
    'application' : True ,
    'license' : 'AGPL-3',
}