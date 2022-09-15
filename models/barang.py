from odoo import api, fields, models


class jajan(models.Model):
    _name = 'h.barang'
    _description = 'deskripsi barang'

    name = fields.Char('nama barang')
    stok = fields.Integer('stok')
    tgl_pembelian = fields.Date('tanggal pembelian')
    harga_jual = fields.Integer('harga jual')

    kateg_id = fields.Many2one('h.barangkateg', string='kategori', ondelete='cascade')

    detailtrx_ids = fields.One2many('h.detailtrx', 'barang_id', string='detail transaksi')


    # def button_clicked(self):
    #     pass