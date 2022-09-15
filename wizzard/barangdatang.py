from odoo import api, fields, models


class BarangDatang(models.TransientModel):
    _name = 'h.barangdatang'
    _description = 'hah'
    
    barang_id = fields.Many2one('h.barang', string='barang', required=True)
    jumlah = fields.Integer('jumlah', required=False)
    
    
    def button_barangdatang(self):
        for z in self:
            self.env['h.barang'].search([('id','=',z.barang_id.id)]).write({'stok': z.barang_id.stok + z.jumlah})