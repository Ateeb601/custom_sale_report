# models/sale_order_line.py

from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    line_note = fields.Text(string="Line Note")
