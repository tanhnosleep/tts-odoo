from odoo import fields, models, api


class Room(models.Model):
    _name = "cinema.room"
    _description = "This is table for room"

    name = fields.Char(required=True, string= 'Tên phòng')
    seat_counts = fields.Integer(compute='_compute_seat_counts', store=True, string= 'Số ghế')

    seat_ids = fields.One2many('cinema.seat', 'room_id', string='Ghế')

    @api.depends('seat_ids')
    def _compute_seat_counts(self):
        for record in self:
            record.seat_counts = len(record.seat_ids)

    @api.model
    def create(self, vals):
        room = super(Room, self).create(vals)
        # Logic to create 120 seats automatically
        rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        for row in rows:
            for num in range(1, 13):  # 12 seats per row
                seat_name = f"{row}{num}"

                # Determine seat type
                if row == 'J':  # Couple seats
                    seat_type = 'Couple'
                elif row in ['E', 'F', 'G', 'H', 'I'] and 3 <= num <= 10:  # Vip seats
                    seat_type = 'Vip'
                else:  # Ordinary seats
                    seat_type = 'Ordinary'

                self.env['cinema.seat'].create({
                    'name': seat_name,
                    'seat_type': seat_type,
                    'room_id': room.id
                })
        return room