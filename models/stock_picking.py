# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def create(self, vals):
        vals.update({'name':False})
        res = super(StockPicking, self).create(vals)
        for picking in res:
            if not picking.picking_type_id.name_assignment_at_validation:
                picking.name = picking.picking_type_id.sequence_id.next_by_id()
        return res

    def _action_done(self):
        res = super(StockPicking, self)._action_done()
        for picking in self:
            if picking.picking_type_id.name_assignment_at_validation:
                picking.name = picking.picking_type_id.sequence_id.next_by_id()
        return res


