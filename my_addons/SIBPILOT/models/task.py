from odoo import models, fields

class Task(models.Model):
    _name = 'task.manager.task'  # Le nom du modèle doit correspondre à celui-ci
    _description = 'Tâche'

    name = fields.Char(string='Titre', required=True)
    description = fields.Text(string='Description')
    due_date = fields.Date(string='Date d\'échéance')
    priority = fields.Selection([
        ('low', 'Basse'),
        ('medium', 'Moyenne'),
        ('high', 'Haute')
    ], string='Priorité', default='medium')
