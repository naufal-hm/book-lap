from email.policy import default
from odoo import api, fields, models
import datetime, time


class Lap(models.Model):
    _name = 'h.lapangan'
    _description = 'detail lapangan'

    id_lapangan = fields.Integer('id lapangan')
    name = fields.Char('nama lapangan')
    jenis_lap = fields.Char('tipe lapangan')
    harga_lap = fields.Integer('harga lapangan')
    # waktu_sibuk = fields.Integer('waktu sibuk')
    waktu_kosong = fields.Datetime('waktu kosong', default=fields.datetime.now())

    field_name = fields.Char(compute='_compute_field_name', string='field_name')




    jenislapangan_id = fields.Many2one('h.jenislapangan', string='jenis lapangan')
    transaksi_id = fields.Many2one('h.trx', string='transaksi')