# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "School",
    "version": "14.0.1.0.0",
    "author": "kush",
    "summary": "School Management System",
    "description": "This is school Management System",
    "depends": ["base","students"],
    "demo": [],
    "category": "School",
    "data": ["security/ir.model.access.csv", "views/views.xml", "views/kp.xml", "views/hobby.xml"],
    "installable": True,
    "auto_install": False,
    "application": True,
}
