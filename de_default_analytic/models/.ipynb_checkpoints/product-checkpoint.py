# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    income_analytic_tag_ids = fields.Many2many('account.analytic.tag', 
                                               relation='your_model_income_analytic_tag_relat',
                                               column1='account_tag_id',
                                               column2='income_analytic_tag_ids',
                                               string="Analytic Tags",)
    expense_analytic_tag_ids = fields.Many2many('account.analytic.tag', 
                                                relation='your_model_expense_analytic_tag_relat',
                                                column1='account_analytic_id',
                                                column2='expense_analytic_tag_ids',
                                                string="Analytic Tags",)


#     @api.multi
    def _get_product_analytic_tags(self):
        self.ensure_one()
        return {
            'income': self.income_analytic_tag_ids or
                      self.categ_id.income_analytic_tag_ids,
            'expense': self.expense_analytic_tag_ids or
                       self.categ_id.expense_analytic_tag_ids
        }

class ProductCategory(models.Model):
    _inherit = 'product.category'

    income_analytic_tag_ids = fields.Many2many('account.analytic.tag', 
                                               relation='your_model_income_analytic_tag_rel',
                                               column1='account_tag_id',
                                               column2='income_analytic_tag_ids',
                                               string="Analytic Tags",)
    expense_analytic_tag_ids = fields.Many2many('account.analytic.tag', 
                                                relation='your_model_expense_analytic_tag_rel',
                                                column1='account_analytic_id',
                                                column2='expense_analytic_tag_ids',
                                                string="Analytic Tags",)


    
    