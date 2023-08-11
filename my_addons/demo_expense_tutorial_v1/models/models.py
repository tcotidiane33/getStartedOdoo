from odoo import models, fields, api
from odoo.exceptions import UserError

class DemoTag(models.Model):
    _name = 'demo.tag'
    _description = 'Demo Tags'
    _rec_name = 'complete_name'

    name = fields.Char(string='Tag Name', index=True, required=True)
    complete_name = fields.Char('Complete Name', compute='_compute_complete_name')
    active = fields.Boolean(default=True, help="Set active.")

    @api.depends('name')
    def _compute_complete_name(self):
        for record in self:
            record.complete_name = 'hello world - {}'.format(record.name)

class DemoExpenseTutorial(models.Model):
    _name = 'demo.expense.tutorial'
    _description = 'Demo Expense Tutorial'
    _order = "sequence, id desc"

    name = fields.Char('Description', required=True)

    # employee_id = fields.Many2one('hr.employee', string="Employee", required=True,
    #             domain=[('active', '=', True)] )
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)

    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)

    # https://www.odoo.com/documentation/12.0/reference/orm.html#odoo.fields.Many2many
    # Many2many(comodel_name=<object object>, relation=<object object>, column1=<object object>, column2=<object object>, string=<object object>, **kwargs)
    #
    # relation: database table name
    #

    # By default, the relationship table name is the two table names
    # joined with an underscore and _rel appended at the end.
    # In the case of our books or authors relationship, it should be named demo_expense_tutorial_demo_tag_rel.


    tag_ids = fields.Many2many('demo.tag', 'demo_expense_tag', 'demo_expense_id', 'tag_id',
        string='Tges', copy=False,
        groups='demo_expense_tutorial_v1.demo_expense_tutorial_group_manager'
    )
    sheet_id = fields.Many2one('demo.expense.sheet.tutorial', string="Expense Report", ondelete='restrict')

    # Related (Reference) fields (不會存在 db)
    # readonly default 為 True
    # store default 為 False
    gender = fields.Selection('Gender', related='employee_id.gender')

    sequence = fields.Integer(index=True, help="Gives the sequence order", default=1)
    active = fields.Boolean(default=True, help="Set active.")
    debug_field = fields.Char('debug_field')
    admin_field = fields.Char('admin_field')

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})
        if not default.get('name'):
            default['name'] = '{} copy'.format(self.name)
        return super(DemoExpenseTutorial, self).copy(default)

    @api.multi
    def button_sheet_id(self):
        return {
            'view_mode': 'form',
            'res_model': 'demo.expense.sheet.tutorial',
            'res_id': self.sheet_id.id,
            'type': 'ir.actions.act_window'
        }

    @api.multi
    def button_rainbow_man(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'hello',
                'type': 'rainbow_man',
            }
        }

    @api.multi
    def btn_test_acid_atomicity(self):
        for index in range(3):
            self.create({
                'name': index,
                'employee_id': 1
            })
            if index == 1:
                raise UserError('error - auto rollback')

    @api.multi
    def button_act_url(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            # 'target': 'self',
            'url': 'https://github.com/twtrubiks/odoo-demo-addons-tutorial',
        }

    @api.multi
    def btn_message_post(self):
        for rec in self:
            if rec.user_id:
                rec.user_id.partner_id.message_post(body="test body", subject="test subject")
            else:
                raise UserError('請選擇使用者(user_id)')

    @api.onchange('user_id')
    def onchange_user_id(self):
        # domain
        result = dict()
        result['domain'] = {
            'employee_id': [('user_id', '=', self.user_id.id)]
        }
        # equal
        # self.env['hr.employee'].search([('user_id', '=', self.user_id.id)])
        return result

class DemoExpenseSheetTutorial(models.Model):
    _name = 'demo.expense.sheet.tutorial'
    _description = 'Demo Expense Sheet Tutorial'

    name = fields.Char('Expense Demo Report Summary', required=True)

    # One2many is a virtual relationship, there must be a Many2one field in the other_model,
    # and its name must be related_field
    expense_line_ids = fields.One2many(
        'demo.expense.tutorial', # related model
        'sheet_id', # field for "this" on related model
        string='Expense Lines')

    demo_expenses_count = fields.Integer(
        compute='_compute_demo_expenses_count',
        string='Demo Expenses Count')

    @api.multi
    def add_demo_expense_record(self):
        # (0, _ , {'field': value}) creates a new record and links it to this one.

        data_1 = self.env.ref('demo_expense_tutorial_v1.demo_expense_tutorial_data_1')

        tag_data_1 = self.env.ref('demo_expense_tutorial_v1.demo_tag_data_1')
        tag_data_2 = self.env.ref('demo_expense_tutorial_v1.demo_tag_data_2')

        for record in self:
            # creates a new record
            val = {
                'name': 'test_data',
                'employee_id': data_1.employee_id,
                'tag_ids': [(6, 0, [tag_data_1.id, tag_data_2.id])]
            }

            self.expense_line_ids = [(0, 0, val)]

    @api.multi
    def link_demo_expense_record(self):
        # (4, id, _) links an already existing record.

        data_1 = self.env.ref('demo_expense_tutorial_v1.demo_expense_tutorial_data_1')

        for record in self:
            # link already existing record
            self.expense_line_ids = [(4, data_1.id, 0)]

    @api.multi
    def replace_demo_expense_record(self):
        # (6, _, [ids]) replaces the list of linked records with the provided list.

        data_1 = self.env.ref('demo_expense_tutorial_v1.demo_expense_tutorial_data_1')
        data_2 = self.env.ref('demo_expense_tutorial_v1.demo_expense_tutorial_data_2')

        for record in self:
            # replace multi record
            self.expense_line_ids = [(6, 0, [data_1.id, data_2.id])]

    @api.multi
    def button_line_ids(self):
        return {
            'name': 'Demo Expense Line IDs',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'demo.expense.tutorial',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'domain': [('sheet_id', '=', self.id)],
        }

    def _compute_demo_expenses_count(self):
        # usually used read_group
        for record in self:
            record.demo_expenses_count = len(self.expense_line_ids)

    @api.multi
    def name_get(self):
        names = []
        for record in self:
            name = '%s-%s' % (record.create_date.date(), record.name)
            names.append((record.id, name))
        return names

    # odoo12/odoo/odoo/addons/base/models/ir_model.py
    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100):
        if args is None:
            args = []
        domain = args + ['|', ('id', operator, name), ('name', operator, name)]
        # domain = args + [ ('name', operator, name)]
        # domain = args + [ ('id', operator, name)]
        return super(DemoExpenseSheetTutorial, self).search(domain, limit=limit).name_get()
