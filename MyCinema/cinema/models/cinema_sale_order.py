from email.policy import default

from odoo import fields, models, api
from odoo.addons.test_convert.tests.test_env import record
from odoo.exceptions import ValidationError, UserError
from odoo.tools.populate import compute


class SaleOrder(models.Model):
    _description = "day la sale order"

    _inherit = 'sale.order.line'
    movie_id = fields.Many2one('cinema.movie')
    show_time_id = fields.Many2one('cinema.show.time', domain="[('movie_id', '=', movie_id)]")
    phong = fields.Char(related='show_time_id.room_name')
    seat_ids = fields.Many2many('cinema.seat', domain="[('room_id', '=', phong),('seat_type', '=', seat_type)]", store = True)
    seat_type = fields.Selection(
        string='Seat Type',
        selection=[('Ordinary', 'Ordinary'), ('Vip', 'Vip'), ('Couple', 'Couple')])
    ticket_ids = fields.Many2many('cinema.ticket', compute='_compute_ticket', store = True)

    product_id = fields.Many2one(related='show_time_id.product_id', store = True)
    product_uom_qty = fields.Float(default = 0.0, compute='_compute_qty')
    price_unit = fields.Float(related='seat_ids.seat_price')
    @api.depends('ticket_ids')
    def _compute_qty(self):
        for record in self:
            record.product_uom_qty = len(record.ticket_ids)

    @api.constrains('seat_ids')
    def _check_seat_type(self):
        for record in self:
            if record.seat_ids:
                # Lấy loại ghế của ghế đầu tiên
                first_seat_type = record.seat_ids[0].seat_type
                # Kiểm tra tất cả các ghế còn lại
                for seat in record.seat_ids:
                    if seat.seat_type != first_seat_type:
                        raise ValidationError(
                            "Tất cả các ghế được chọn phải có cùng loại ghế."
                        )

    @api.depends('seat_ids', 'show_time_id')
    def _compute_ticket(self):
        for record in self:
            if record.seat_ids and record.show_time_id:
                # Tìm các vé tương ứng với showtime và các ghế đã chọn
                tickets = self.env['cinema.ticket'].search([
                    ('show_time_id', '=', record.show_time_id.id),
                    ('seat_id', 'in', record.seat_ids.ids)
                ])
                record.ticket_ids = tickets
                # Kiểm tra trạng thái "Sold"
                for ticket in record.ticket_ids:
                    if ticket.sold_status == 'Sold':
                        raise ValidationError(
                            "Vé đã được bán, vui lòng chọn vé khác."
                        )

                # Gán khách hàng vào vé
                for ticket in record.ticket_ids:
                    ticket.customer_id = record.order_partner_id
            else:
                record.ticket_ids = False