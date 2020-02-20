# -*- coding: utf-8 -*-
# from odoo import http


# class Elguey(http.Controller):
#     @http.route('/elguey/elguey/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/elguey/elguey/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('elguey.listing', {
#             'root': '/elguey/elguey',
#             'objects': http.request.env['elguey.elguey'].search([]),
#         })

#     @http.route('/elguey/elguey/objects/<model("elguey.elguey"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('elguey.object', {
#             'object': obj
#         })
