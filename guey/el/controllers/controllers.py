# -*- coding: utf-8 -*-
# from odoo import http


# class El(http.Controller):
#     @http.route('/el/el/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/el/el/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('el.listing', {
#             'root': '/el/el',
#             'objects': http.request.env['el.el'].search([]),
#         })

#     @http.route('/el/el/objects/<model("el.el"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('el.object', {
#             'object': obj
#         })
