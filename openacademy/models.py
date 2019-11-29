from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'
    _description = "OpenAcademy Courses"

    # _rec_name = 'description'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    description2 = fields.Text()
    description3 = fields.Text()


    state = fields.Selection([
    		('draft', 'Draft'),
    		('confirmed', 'Confirmed'),
    		('done', 'Done'),
    	], default='draft')


class Session(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")