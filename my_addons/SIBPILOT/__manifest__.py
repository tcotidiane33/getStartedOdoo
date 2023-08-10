{
    'name': 'SIBPILOT Gestionnaire de tâches',
    'summary': 'v0.1 Module exemple pour gérer des tâches.',
    'description': 'Un exemple de module Odoo pour gérer des tâches.',
    'author': 'Eureka',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'views/task_views.xml',
        'security/ir.model.access.csv',
    ],
    'application': True,
}
