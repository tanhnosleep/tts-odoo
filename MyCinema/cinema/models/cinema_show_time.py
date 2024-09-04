from email.policy import default
from datetime import timedelta, datetime
from odoo import fields, models, api
from odoo.addons.test_convert.tests.test_env import record
from odoo.fields import Datetime
from odoo.tools.populate import compute
import pytz

class ShowTime(models.Model):
    _name = "cinema.show.time"
    _description = "This is table for show time"

    name = fields.Text(default='Xuat Chiếu Phim')
    begin_time = fields.Datetime(string = 'Giờ bắt đầu',  default=datetime.today())
    movie_id = fields.Many2one('cinema.movie', string='Phim')
    movie_name = fields.Char(related = 'movie_id.name')
    thoi_luong = fields.Integer(related='movie_id.length')
    end_time = fields.Datetime(compute='_compute_end_time', string = 'Giờ kết thúc')
    room_id = fields.Many2one('cinema.room', string='Phòng')
    room_name = fields.Char(related='room_id.name')

    @api.depends("begin_time", "thoi_luong")
    def _compute_end_time(self):
        for record in self:
            record.end_time = record.begin_time + timedelta(minutes=record.thoi_luong)
