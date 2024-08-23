from odoo import fields, models


class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "This is demo for estate_property_tag"

    name = fields.Char(required=True)