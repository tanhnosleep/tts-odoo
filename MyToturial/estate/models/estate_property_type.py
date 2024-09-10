
from odoo import fields, models


class RecurringPlan(models.Model):
    _name = "estate.property.type"
    _description = "This is demo for estate_property_type"
    _order = "sequence, name asc"
    _sql_constraints = [
        ('check_type_name', 'unique(name)',
         'The property type name must be unique.')
    ]

    sequence = fields.Integer('Sequence', default=1)
    name = fields.Char(required=True)
    estate_ids = fields.One2many('estate.property', 'property_type_id', string = 'estate_ids')
