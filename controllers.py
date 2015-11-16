# -*- coding: utf-8 -*-
from openerp import http

# class Azizmodule(http.Controller):
#     @http.route('/azizmodule/azizmodule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/azizmodule/azizmodule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('azizmodule.listing', {
#             'root': '/azizmodule/azizmodule',
#             'objects': http.request.env['azizmodule.azizmodule'].search([]),
#         })

#     @http.route('/azizmodule/azizmodule/objects/<model("azizmodule.azizmodule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('azizmodule.object', {
#             'object': obj
#         })