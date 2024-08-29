from odoo import fields, models


class Movie(models.Model):
    _name = "movie"
    _description = "This is table for movie"

    name = fields.Char(required=True, string= 'Tên phim')
    content = fields.Text(string= 'Nội dung')
    length= fields.Integer(string= 'Thời lượng (phút)')

    show_time_ids = fields.Many2many('show.time', string='xuat chieu')
    category_ids = fields.Many2many('movie.category', string='Thể loại')
    actor_ids = fields.Many2many('movie.actor', string='Diễn viên chính')