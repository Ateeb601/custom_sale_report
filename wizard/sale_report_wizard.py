from odoo import models, fields
from datetime import datetime

class SaleOrderReportWizard(models.TransientModel):
    _name = 'sale.order.report.wizard'
    _description = 'Wizard for Sale Order Report'

    date_from = fields.Date(string="Date From", required=True)
    date_to = fields.Date(string="Date To", required=True)

    def action_print_report(self):
        sale_orders = self.env['sale.order'].search([
            ('date_order', '>=', self.date_from),
            ('date_order', '<=', self.date_to),
        ])
        return self.env.ref('custom_sale_report.action_sale_order_report').report_action(sale_orders)
# 'custom_sale_report.action_sale_order_report'  =  our_module_name.report/sale_report_template.xml

# report_action() Odoo ka built-in method hai, jo ir.actions.report model ka part hai. Is method ka kaam hai:
# Odoo ko batata hai ke konsi records pe konsi report run karni hai.

