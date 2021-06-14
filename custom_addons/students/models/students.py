# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    order_id = fields.Char(string="OrderID")
    cancel_order = fields.Char(string="Cancel Order")


class StudentsProfile(models.Model):
    _name = "students.profile"
    _description = "students.profile"
    _rec_name = "phone"

    name = fields.Char(string="Student Name", required=True)
    email = fields.Char(string="Student Email")
    phone = fields.Char(string="Student Phone Number")
    result = fields.Float(string="Student Result")
    student_in_class = fields.Boolean(
        string="Student is present in class", required=True
    )
    student_address = fields.Text(string="Student Address")
    student_birthdate = fields.Date(string="Student Birthdate")
    student_school_joiningdate = fields.Datetime(string="Student School Joining date")
    school_type = fields.Selection(
        [("Public", "Public School"), ("private", "private school")],
        string="Type Of School",
    )
    student_documents = fields.Binary(string="Student Documents")
    student_image = fields.Image(
        string="Upload Student Image", max_width=100, max_hight=100
    )
    student_description = fields.Html(string="Student Description")
    student_note = fields.Text(string="Student Note")
    assignment_note = fields.Text(string="Assignment Note")

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

    def name_get(self):
        student_list = []
        for school in self:
            name = school.name
            if school.school_type:
                name += "({})".format(school.school_type)
            student_list.append((school.id, name))
        return student_list
