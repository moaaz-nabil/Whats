from odoo import models, fields, api , _
from odoo.exceptions import ValidationError

class WhatsApp_Messege(models.TransientModel):
    _name = 'whatsapp.messegecontacts'

    user = fields.Many2one('res.partner', string="User", required=True)
    mobile = fields.Char(related='user.mobile', string="Mobile", required=True)
    message = fields.Text(string="Message", required=True)

    def send_message_whats(self):
        if self.mobile and self.message :
            message_string = ''
            message = self.message.split(' ')
            for msg in message:
                message_string = message_string + msg + '%20'
            message_string = message_string[:(len(message_string)-3)]
            return {
                'type' : 'ir.actions.act_url',
                'url' : "https://web.whatsapp.com/send?phone="+self.user.mobile+"&text=" + message_string,
                'target' : 'new',

            }
