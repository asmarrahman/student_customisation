# -*- coding: utf-8 -*-
# from odoo import http


# class NewCustModule(http.Controller):
#     @http.route('/new_cust_module/new_cust_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_cust_module/new_cust_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_cust_module.listing', {
#             'root': '/new_cust_module/new_cust_module',
#             'objects': http.request.env['new_cust_module.new_cust_module'].search([]),
#         })

#     @http.route('/new_cust_module/new_cust_module/objects/<model("new_cust_module.new_cust_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_cust_module.object', {
#             'object': obj
#         })
