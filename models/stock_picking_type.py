# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    name_assignment_at_validation = fields.Boolean(string='Reference assignment at validation',default=False,help='If we want to assigne the reference of the picking at the validation operation')