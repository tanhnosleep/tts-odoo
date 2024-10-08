from datetime import timedelta

from odoo import http, fields, models, tools
from odoo.http import request


class CinemaController(http.Controller):
    @http.route('/cinema', type='http', auth='public', website=True)
    def cinema(self):
        some_movies = http.request.env['cinema.movie'].search([])
        data = {
            'model': some_movies,
        }
        return http.request.render("cinema.someTemplate", data)

    @http.route('/cinema/movie/<int:movie_id>', type='http', auth='public', website=True)
    def movie_detail(self, movie_id):
        movie = http.request.env['cinema.movie'].sudo().browse(movie_id)
        showtimes = http.request.env['cinema.show.time'].sudo().search([('movie_id', '=', movie_id)])

        data = {
            'movie': movie,
            'showtimes': showtimes
        }
        return http.request.render("cinema.movie_detail_template", data)

    @http.route('/cinema/movie/<int:movie_id>/booking/<int:showtime_id>', type='http', auth='public', website=True)
    def movie_booking(self, showtime_id, movie_id):
        showtime_data = http.request.env['cinema.show.time'].sudo().browse(showtime_id)
        movie = http.request.env['cinema.movie'].sudo().browse(movie_id)
        data = {
            'showtime_data': showtime_data,
            'movie': movie,
        }
        return http.request.render("cinema.cinema_booking", data)
