{
    'name': 'My Bank Module',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Your Name',
    'category': 'Custom',
    'data': [
        'security/ir.model.access.csv',
        'views/bank_manager_views.xml',
        'data/bank_manager_data.xml',  # Inclure le fichier de données ici
    ],
    'application': True,
}
