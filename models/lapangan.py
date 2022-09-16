from odoo import api, fields, models
import time
from datetime import datetime


class Lap(models.Model):
    _name = 'h.lapangan'
    _description = 'detail lapangan'

    id_lapangan = fields.Integer('id lapangan')
    name = fields.Char('nama lapangan')
    jenis_lap = fields.Char('tipe lapangan')
    harga_lap = fields.Integer('harga lapangan')
    # waktu_sibuk  fields.Integer('waktu sibuk')
    waktu_kosong = fields.Datetime('waktu kosong', default=fields.datetime.now())

    waktu = fields.Datetime('waktu', default=datetime.now())
    waku = fields.Datetime('waku', default=datetime.now())
    @api.onchange('waktu')
    def _onchange_waktu(self):
        if self.waktu < self.waku:
            self.waktu = self.waku
            return{
                'warning':{
                    'title':'warning',
                    'message':'tidak dapat memilih kemarin'
                }
            }

    jenislapangan_id = fields.Many2one('h.jenislapangan', string='jenis lapangan')
    transaksi_id = fields.Many2one('h.trx', string='transaksi')