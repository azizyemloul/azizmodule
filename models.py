# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class azizmodule(models.Model):
#     _name = 'azizmodule.azizmodule'

#     name = fields.Char()


class Course(models.Model):
    _name = 'azizmodule.course'
    
    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    responsible_id = fields.Many2one(
        'res.users', ondelete='set null', string="Responsible", index=True)
    
    session_ids = fields.One2many(
        'azizmodule.session', 'course_id', string="Sessions")
    
class Session(models.Model):
    _name ='azizmodule.session'
    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
        

    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one(
        'azizmodule.course', ondelete='cascade', string="Course", required=True)
    
        
