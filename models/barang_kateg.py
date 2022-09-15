from odoo import api, fields, models


class kateg(models.Model):
    _name = 'h.barangkateg'
    _description = 'kategori barang'

    name = fields.Char('name')
    kategori = fields.Char('kategori')
    kode_kateg = fields.Char('kode kategori')

    barang_ids = fields.One2many('h.barang', 'kateg_id', string='barang')