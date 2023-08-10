from odoo import http
from odoo.http import request

class BankManagerController(http.Controller):

    @http.route('/my_bank_module/bank_managers', type='http', auth='user', website=True)
    def list_bank_managers(self, **kwargs):
        bank_managers = request.env['bank.manager'].sudo().search([])
        return http.request.render('my_bank_module.bank_manager_list', {'bank_managers': bank_managers})
