# -*- coding: utf-8 -*-

 from odoo import models, fields


class elguey1(models.Model):
      name = 'elguey1.elguey1'
     _description = 'elguey1.elguey1'

    Nombre = fields.Char()
    Valor = fields.Integer()
    Costo = fields.Float(compute="_value_pc", store=True)
    Categoria = fields.Text()
    Precio de Venta = fields.float()
    Tipo = fields.Text()
    
    
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
