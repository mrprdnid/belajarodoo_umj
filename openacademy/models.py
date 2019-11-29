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

    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")

class Session(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")	

    def compute_jumlah_peserta(self):
    	for rec in self:
    		rec.jumlah_peserta = len(rec.attendee_ids)
    jumlah_peserta = fields.Integer(compute=compute_jumlah_peserta)

    @api.onchange('attendee_ids')
    def compute_jumlah_peserta2(self):
    	for rec in self:
    		rec.jumlah_peserta2 = len(rec.attendee_ids)
    jumlah_peserta2 = fields.Integer()

    def compute_sisa_kursi(self):
    	for rec in self:
    		rec.sisa_kursi = rec.seats - len(rec.attendee_ids)
    sisa_kursi = fields.Integer(compute=compute_sisa_kursi)



class InheritCourse1(models.Model):
	_inherit = 'openacademy.course'

	warna = fields.Selection([
		('merah', 'Merah'),
		('biru', 'Biru'),
		('kuning', 'Kuning'),
		])

class InheritCourse2(models.Model):
	_name = 'openacademy.inherit2'
	_inherit = 'openacademy.course'

	tingkat = fields.Selection([
			('sd', 'SD'),
			('smp', 'SMP'),
			('sma', 'SMA'),
		])
