from email.policy import default
from datetime import timedelta, datetime
from odoo import fields, models, api
from odoo.addons.test_convert.tests.test_env import record
from odoo.fields import Datetime
from odoo.tools.populate import compute
import pytz

class ShowTime(models.Model):
    _name = "show.time"
    _description = "This is table for show time"

    name = fields.Selection(
        string='Xuất chiếu',
        selection=[('Xuất sáng', 'Xuất sáng'), ('Xuất trưa', 'Xuất trưa'), ('Xuất chiều', 'Xuất chiều'), ('Xuất tối', 'Xuất tối'), ('Xuất khuya', 'Xuất khuya')],
        required=True, copy=False, default='Xuất sáng')
    begin_time = fields.Datetime(string = 'Giờ bắt đầu', compute='_computed_begin_time', readonly = False)
    movie_id = fields.Many2one('movie', string='Phim')
    thoi_luong = fields.Integer(related='movie_id.length')

    end_time = fields.Datetime(compute='_compute_end_time', string = 'Giờ kết thúc')

    @api.depends("begin_time", "thoi_luong")
    def _compute_end_time(self):
        for record in self:
            record.end_time = record.begin_time + timedelta(minutes=record.thoi_luong)

    @api.depends("name")
    def _computed_ticket_price(self):
        for record in self:
            if record.name == 'Xuất sáng':
                record.adult_ticket_price = 70000
                record.children_ticket_price = 50000
            if record.name == 'Xuất trưa':
                record.adult_ticket_price = 80000
                record.children_ticket_price = 60000
            if record.name == 'Xuất chiều':
                record.adult_ticket_price = 90000
                record.children_ticket_price = 70000
            if record.name == 'Xuất tối':
                record.adult_ticket_price = 85000
                record.children_ticket_price = 65000
            if record.name == 'Xuất khuya':
                record.adult_ticket_price = 60000
                record.children_ticket_price = 40000

    @api.depends("name")
    def _computed_begin_time(self):
        for record in self:
            if record.name == 'Xuất sáng':
                record.begin_time = datetime.now().replace(hour=8, minute=0, second=0) - timedelta(minutes=7*60)
            if record.name == 'Xuất trưa':
                record.begin_time = datetime.now().replace(hour=12, minute=0, second=0)- timedelta(minutes=7*60)
            if record.name == 'Xuất chiều':
                record.begin_time = datetime.now().replace(hour=16, minute=0, second=0)- timedelta(minutes=7*60)
            if record.name == 'Xuất tối':
                record.begin_time = datetime.now().replace(hour=21, minute=0, second=0)- timedelta(minutes=7*60)
            if record.name == 'Xuất khuya':
                record.begin_time = datetime.now().replace(hour=23, minute=30, second=0)- timedelta(minutes=7*60)

    seat_counts = fields.Integer(default = 50, required = True, string= 'Số ghế ')
    adult_ticket_price = fields.Float(compute='_computed_ticket_price', string= 'Giá vé người lớn')
    children_ticket_price = fields.Float(compute='_computed_ticket_price', string= 'Giá vé trẻ em')

