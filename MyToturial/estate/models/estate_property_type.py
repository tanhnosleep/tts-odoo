
from odoo import fields, models


class RecurringPlan(models.Model):
    _name = "estate.property.type"
    _description = "This is demo for estate_property_type"

    name = fields.Char(required=True)
    estate_ids = fields.One2many('estate.property', 'property_type_id', string = 'estate_ids')
