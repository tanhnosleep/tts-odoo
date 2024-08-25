from odoo import fields, models


class MovieCategory(models.Model):
    _name = "movie.category"
    _description = "This is table for movie category"

    name = fields.Text(required = True)