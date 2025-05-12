from odoo import models

class SaleOrderReport(models.AbstractModel):
    _name = 'report.custom_sale_report.sale_order_template'
    _description = 'Sale Order Custom Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['sale.order'].browse(docids)
        return {
            'docs': docs,
        }
