from email.policy import default
from odoo import api, fields, models


class member(models.Model):
    _name = 'h.member'
    _description = 'desk member'

    name = fields.Char('name')
    expiret = fields.Date('expired')
    waktu_sisa = fields.Integer('sisa waktu')
    point = fields.Float('point')

    transaksi_ids = fields.One2many('h.trx', 'name', string='transaksi')