from odoo import fields, models


class MovieCategory(models.Model):
    _name = "movie.category"
    _description = "This is table for movie category"

    name = fields.Text(required = True)
    movie_ids = fields.Many2many('movie', string='Phim')