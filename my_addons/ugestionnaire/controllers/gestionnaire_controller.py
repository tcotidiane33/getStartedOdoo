from odoo import http
from odoo.http import request


class GestionnaireController(http.Controller):

    @http.route('/gestionnaire', type='http', auth='public', website=True)
    def gestionnaire_page(self):
        gestionnaires = request.env['module_gestionnaire.gestionnaire'].sudo().search([])
        return request.render('module_gestionnaire.gestionnaire_template', {'gestionnaires': gestionnaires})