from odoo import models, fields, api ,_
from datetime import date
from dateutil.relativedelta import relativedelta

class Student(models.Model):
    _name = 'new_cust_module.student'
    _description = 'New Cust Module Student'

    name = fields.Char(string='Name', required=True, tracking=True)
    dob = fields.Date(string='Date of Birth', tracking=True)
    age = fields.Integer(string='Age', compute='_compute_age', store=True, tracking=True)
    classes = fields.Char(string='Class', tracking=True)
    image = fields.Binary(string='Image', tracking=True)
    sequence = fields.Char(string='Sequence', required=True, copy=False, readonly=True, default=lambda self: _('New'))


    @api.depends('dob')
    def _compute_age(self):
        print("============self===============",self)
        for record in self:
            delta = relativedelta(date.today(), record.dob)
            print("===========delta===========",delta)
            record.age = delta.years

    @api.model
    def create(self, vals):
        print("In create vals: ",vals)
        if vals.get('sequence', _('New')) == _('New'):
            vals['sequence'] = self.env['ir.sequence'].next_by_code('new_cust_module.student') or _('New')
        return super(Student, self).create(vals)
    