# -*- coding: utf-8 -*-
from odoo import http

# class ResumenFcobro(http.Controller):
#     @http.route('/summary_payment_terms/summary_payment_terms/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/summary_payment_terms/summary_payment_terms/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('summary_payment_terms.listing', {
#             'root': '/summary_payment_terms/summary_payment_terms',
#             'objects': http.request.env['summary_payment_terms.summary_payment_terms'].search([]),
#         })

#     @http.route('/summary_payment_terms/summary_payment_terms/objects/<model("summary_payment_terms.summary_payment_terms"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('summary_payment_terms.object', {
#             'object': obj
#         })