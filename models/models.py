# -*- coding: utf-8 -*-

from odoo import models, fields, api

class whatsapp_messege(models.Model):
    _inherit = 'res.partner'


    def wizard_whats_messege (self):
        return{'type': 'ir.actions.act_window',
               'name' : 'Whats App Messege',
               'res_model' : 'whatsapp.messegecontacts',
               'target' : 'new',
               'view_type' : 'form',
               'view_mode' : 'form' 
               } 