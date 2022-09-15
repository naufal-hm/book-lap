# -*- coding: utf-8 -*-
# from odoo import http


# class Halosport(http.Controller):
#     @http.route('/halosport/halosport', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/halosport/halosport/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('halosport.listing', {
#             'root': '/halosport/halosport',
#             'objects': http.request.env['halosport.halosport'].search([]),
#         })

#     @http.route('/halosport/halosport/objects/<model("halosport.halosport"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('halosport.object', {
#             'object': obj
#         })
