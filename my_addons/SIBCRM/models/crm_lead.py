from odoo import models, fields, api


class CrmLead(models.Model):
    _name = 'crm.lead'
    _description = 'Opportunité'

    name = fields.Char(string='Nom', required=True)
    partner_id = fields.Many2one('res.partner', string='Client')
    stage_id = fields.Many2one('crm.stage', string='Étape')
    user_id = fields.Many2one('res.users', string='Responsable')
    description = fields.Text(string='Description')


class CrmStage(models.Model):
    _name = 'crm.stage'
    _description = 'Étape CRM'

    name = fields.Char(string='Nom', required=True)
