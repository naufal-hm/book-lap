from odoo import api, models, fields


class jenis(models.Model):
    _name = 'h.jenislapangan'
    _description = 'jenis lapangan'

    name = fields.Char('jenis lapangan')
    lokasi = fields.Char('lokasi')
    
    lapangan_ids = fields.One2many('h.lapangan', 'jenislapangan_id', string='lapangan')