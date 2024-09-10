from odoo import fields, models


class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "This is demo for estate_property_tag"
    _order = "name asc"
    _sql_constraints = [
        ('check_tag_name', 'unique(name)',
         'The property tag name must be unique.')
    ]
    name = fields.Char(required=True)