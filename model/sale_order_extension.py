from odoo import models, fields, api



class SaleOrderExtension(models.Model):
    _inherit = 'sale.order'

    appointment_id = fields.Date(string='Appointment')



    def action_open_sale_report_wizard(self):   # is button k through wizard open ho jae ga aur is button ko view/sale_order_view.xml me bhi define krna h
        return {
            'name': 'Sale Report',
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order.report.wizard',  # ye model ka naam ha jo k wizard/sale_report_wizard.py me define ha
            'view_mode': 'form',
            'target': 'new',
        }

    mobile = fields.Char(string='Phone Number', required=True, tracking=True)  # Mobile number (tracked)
    email = fields.Char(string='Email', required=True, tracking=True)  # Email address (tracked)
    dob = fields.Date(string='Date of Birth')  # Patient's date of birth
    address = fields.Char(string='Address', required=True, tracking=True)  # Address (tracked)

    line_note = fields.Text(string="Line Note")

