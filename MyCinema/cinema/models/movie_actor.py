from odoo import fields, models


class MovieActor(models.Model):
    _name = "movie.actor"
    _description = "This is table for movie actor"

    name = fields.Text(required = True)