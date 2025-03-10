from odoo import fields, models


class Movie(models.Model):
    _name = "cinema.movie"
    _description = "This is table for movie"

    name = fields.Char(required=True, string= 'Tên phim')
    content = fields.Text(string= 'Nội dung')
    length= fields.Integer(string= 'Thời lượng (phút)')

    show_time_ids = fields.One2many('cinema.show.time','movie_id', string='xuat chieu')
    category_ids = fields.Many2many('cinema.movie.category', string='Thể loại')
    actor_ids = fields.Many2many('cinema.movie.actor', string='Diễn viên chính')
    sale_order_ids = fields.One2many('sale.order.line', 'movie_id')

    poster = fields.Binary(string='Poster', attachment=True)
    trailer = fields.Text(string= 'Trailer')