{
    'name': "Votre Module CRM Personnalisé",
    'summary': "Description sommaire de votre module.",
    'description': "Description détaillée de votre module.",
    'author': "Votre nom",
    'category': 'CRM',
    'version': '0.1',
    'depends': ['base', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_views.xml',
        'views/crm_templates.xml',
        'data/crm_demo.xml',  # Ajout du fichier demo
    ],
    'demo': [
        'demo/crm_demo.xml',  # Ajout du fichier demo
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': ['static/src/xml/*.xml'],
    'post_init_hook': 'post_init_hook',
}
