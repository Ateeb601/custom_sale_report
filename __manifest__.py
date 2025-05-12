{
    'name': 'Custom Sale Report',
    'version': '1.0',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'view/sale_order_view.xml',
        'wizard/sale_report_wizard_view.xml',
        'report/sale_report_template.xml',
    ],
    'installable': True,
}
