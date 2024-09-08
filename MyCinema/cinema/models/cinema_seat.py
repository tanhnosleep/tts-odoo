from odoo import fields, models, api


class Foods(models.Model):
    _name = "cinema.seat"
    _description = "This is table for seat"

    seat_name = fields.Char()
    seat_type = fields.Selection(
        string='Seat Type',
        selection=[('Ordinary', 'Ordinary'), ('Vip', 'Vip'), ('Couple', 'Couple')],
        required=True, default='Ordinary')
    seat_price = fields.Float(compute='_compute_seat_price', string='Giá ghế')

    @api.depends("seat_type")
    def _compute_seat_price(self):
        for record in self:
            if record.seat_type == 'Ordinary':
                record.seat_price = 70000
            if record.seat_type == 'Vip':
                record.seat_price = 100000
            if record.seat_type == 'Couple':
                record.seat_price = 130000

    room_id = fields.Many2one('cinema.room', string='Phòng')
    sale_order_ids = fields.One2many('sale.order.line', 'seat_id')