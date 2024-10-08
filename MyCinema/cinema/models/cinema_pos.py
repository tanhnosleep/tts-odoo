from odoo import models

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _pos_ui_models_to_load(self):
        res = super()._pos_ui_models_to_load()
        res.append('cinema.movie')  # Nạp model phim vào POS
        return res

    def _get_pos_ui_custom_model(self, params):
        return self.env['cinema.movie'].search_read(**params['search_params'])