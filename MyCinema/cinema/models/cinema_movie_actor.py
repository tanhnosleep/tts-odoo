from odoo import fields, models


class MovieActor(models.Model):
    _name = "cinema.movie.actor"
    _description = "This is table for movie actor"

    name = fields.Text(required = True)
    movie_ids = fields.Many2many('cinema.movie', string='Phim')