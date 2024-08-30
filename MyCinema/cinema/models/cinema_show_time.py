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

    name = fields.Text(default='Giờ Chiếu Phim')
    begin_time = fields.Datetime(string = 'Giờ bắt đầu',  default=datetime.today())
    movie_ids = fields.Many2many('cinema.movie', string='Phim')
    thoi_luong = fields.Integer(related='movie_ids.length')
    end_time = fields.Datetime(compute='_compute_end_time', string = 'Giờ kết thúc')

    @api.depends("begin_time", "thoi_luong")
    def _compute_end_time(self):
        for record in self:
            record.end_time = record.begin_time + timedelta(minutes=record.thoi_luong)
