# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Students",
    'version': "14.0.1.0.0",
    'author': "kush",
    'summary': "Students Management System", 
    'description': "This is Students Management System",
    'depends': ['sale'],
    'demo': [],
    'category': 'Students',
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/salenote.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
