from odoo import models, fields

class Gestionnaire(models.Model):
    _name = 'module_gestionnaire.gestionnaire'
    _description = 'Gestionnaire Model'

    name = fields.Char(string='Nom', required=True)
    matricule = fields.Char(string='Matricule')
    pole = fields.Char(string='Pôle')
    entreprise = fields.Char(string='Entreprise')