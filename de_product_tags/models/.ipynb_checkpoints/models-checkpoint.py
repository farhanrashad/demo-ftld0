# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Product(models.Model):
    _inherit = 'product.product'
    
    tag_ids = fields.Many2many('product.tags', string='Tags',readonly=True, store=True)

class ProductTags(models.Model):
    _name = 'product.tags'
    _description = 'Product Tags'
    
    name = fields.Char(string="Tag Name", required=True)

