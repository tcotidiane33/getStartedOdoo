from odoo import fields, models

class BankManager(models.Model):
    _name = 'bank.manager'
    _description = 'Bank Manager'

    name = fields.Char(string='Name', required=True)
    responsibilities = fields.Text(string='Responsibilities')
    deals_count = fields.Integer(string='Deals Count')

    # You can define more fields as needed
