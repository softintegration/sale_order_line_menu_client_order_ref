# -*- coding: utf-8 -*-

from odoo import models,fields,api,_
from odoo.exceptions import UserError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    client_order_ref = fields.Char(related='order_id.client_order_ref',string='Customer Reference',)