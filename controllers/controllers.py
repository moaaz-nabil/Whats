# -*- coding: utf-8 -*-
from odoo import http

# class WhatsappMessege(http.Controller):
#     @http.route('/whatsapp_messege/whatsapp_messege/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/whatsapp_messege/whatsapp_messege/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('whatsapp_messege.listing', {
#             'root': '/whatsapp_messege/whatsapp_messege',
#             'objects': http.request.env['whatsapp_messege.whatsapp_messege'].search([]),
#         })

#     @http.route('/whatsapp_messege/whatsapp_messege/objects/<model("whatsapp_messege.whatsapp_messege"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('whatsapp_messege.object', {
#             'object': obj
#         })