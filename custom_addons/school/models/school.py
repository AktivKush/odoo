# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    live = fields.Boolean(string="Live in USA")
    total_tax = fields.Integer(string="Total Tex Pay")


# class SaleOrderin(models.Model):
#     _inherit="school.info"

#     name=fields.Char(string="SchoolInfo")


class SchoolProfile(models.Model):
    _name = "school.profile"
    _description = "school.profile"

    name = fields.Char(string="SchoolName", required=True)
    email = fields.Char(string="Email", required=True, default="abc@gmail.com")
    phone = fields.Char(string="Phone", required=True, size=10)
    is_virtual_class = fields.Boolean(
        string="Virtual Class Support?", help="Class is online/offline", required=True
    )
    school_rank = fields.Integer(string="Rank")
    result = fields.Float(string="Result")
    address = fields.Text(
        related="student_id.student_address", string="Student Address"
    )
    estalish_date = fields.Date(string="Estalish Date", default=fields.Date.today())
    open_date = fields.Datetime("Open Date")
    school_type = fields.Selection(
        [("Public", "Public School"), ("private", "private school")],
        string="Type Of School",
    )
    location = fields.Selection(
        [
            ("Ah", "Ahmedabad"),
            ("Gn", "Gandhinagar"),
            ("Su", "Surat"),
            ("Rj", "Rajkot"),
            ("Vd", "Vadodara"),
        ],
        string="School Location",
    )
    documents = fields.Binary(string="Documents")
    school_image = fields.Image(
        string="Upload School Image", max_width=100, max_hight=100
    )
    school_description = fields.Html(string="Description")
    schoolnote = fields.Text(string="School_Note")
    teachernote = fields.Text(string="Teacher_Note")
    student_id = fields.Many2one("students.profile", string="Students Name")
    student_list = fields.One2many("students.profile", "phone", string="Students List")
    hobby_list = fields.Many2many(
        "hobby", "student_hobby_rel", "school_id", "hobby_id", string="Hobby List"
    )
    appoinment_list = fields.One2many(
        "school.profile.line", "school_id", string="Appoinment Lists"
    )
    techer_ids = fields.Many2many(
        "students.profile", "student_teacher_rel", string="Teachers"
    )


class SchoolProfileLine(models.Model):
    _name = "school.profile.line"
    _description = "school.profile.line"

    student_id = fields.Many2one("students.profile", string="Student Id")
    total_parent = fields.Integer(string="Total Parent")
    school_id = fields.Many2one("school.profile", string="School Id")


# class StudentsProfile(models.Model):
#     _inherit = "students.profile"

#     student_list = fields.One2many("school.profile","student_id",string="Students List")


class Hobbies(models.Model):
    _name = "hobby"

    hobby_name = fields.Char(string="Hobby")
