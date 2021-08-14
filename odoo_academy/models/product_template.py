# -*- coding: utf-8 -*-
from odoo import models, fields, api
class ProductTemplate(models.Model):
    
    _inherit = 'product.template'
    
    id_session_product = fields.Boolean(string='Use a Session Product',
                                        help='Check this box to use this as a Product for Session Fee',
                                        default=False)