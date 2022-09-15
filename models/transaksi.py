from email.policy import default
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class trx(models.Model):
    _name = 'h.trx'
    _detail = 'trxnya'

    # name = fields.Char('name pembeli')
    waktu = fields.Integer('waktu (dalam satuan jam)')
    non_member = fields.Char('non member')
    no_nota = fields.Integer('no nota')
    name = fields.Many2one('h.member', string='member')
    tgl_penjualan = fields.Datetime('tanggal penjualan')
    lapangan_id = fields.Many2one('h.lapangan', string='lapangan')
    total_bayar = fields.Char(compute='_compute_total_bayar', string='total bayar')

    detailtrx_ids = fields.One2many('h.detailtrx', 'trx_id', string='detail transaksi')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancelled', 'Cancel'),
        ('confirm', 'Confirm')
    ], string='state', required=True, readonly=True, default='draft')

    # gift point to member
    @api.model
    def create(self, vals):
        record = super(trx, self).create(vals)
        if record.waktu:
            self.env['h.member'].search([('id', '=', record.name.id)]).write({'point': record.name.point + (record.waktu /2), 'waktu_sisa': record.name.waktu_sisa - record.waktu})
        return record


    #compute total bayar
    @api.depends('detailtrx_ids')
    def _compute_total_bayar(self):
        for z in self:
            a = sum(self.env['h.detailtrx'].search([('trx_id', '=', z.id)]).mapped('sub_total'))
            z.total_bayar += a
        self.total_bayar = (int(self.lapangan_id.harga_lap) + int(self.total_bayar))

    #balikin stok
    @api.ondelete(at_uninstall=False)
    def _ondelete_penjualan(self):
        if self.filtered(lambda line:line.state != 'draft'):
            raise ValidationError('hanya draft dihapus')
        if self.detailtrx_ids:
            a = []
            for z in self:
                a = self.env['h.detailtrx'].search([('trx_id', '=', z.id)])
            for obj in a:
                obj.barang_id.stok += obj.qty

    #edit penjualan
    def write(self, vals):
        #ambil value di penjualan
        for z in self:
            a = self.env['h.detailtrx'].search([('trx_id', '=', z.id)])
            for data in a:
                data.barang_id.stok += data.qty
        rec = super(trx,self).write(vals)
        for z in self:
            b = self.env['h.detailtrx'].search([('trx_id', '=', z.id)])
            for data in b:
                if data in a:
                    data.barang_id.stok -= data.qty
                else: pass
        return rec



    def st_button_confirm(self):
        self.write({'state': 'confirm'})
    def st_button_done(self):
        self.write({'state': 'done'})
    def st_button_draft(self):
        self.write({'state': 'draft'})
    def st_button_cancel(self):
        self.write({'state': 'cancelled'})


    


class dtrx(models.Model):
    _name = 'h.detailtrx'
    _description = 'h.dtrx'

    name = fields.Char('name')
    trx_id = fields.Many2one('h.trx', string='trx id')
    barang_id = fields.Many2one('h.barang', string='barang')
    harga_satuan = fields.Integer('harga_satuan')
    qty = fields.Integer('qty')
    sub_total = fields.Integer(compute='_compute_sub_total', string='sub_total')
    
    @api.depends('qty', 'harga_satuan')
    def _compute_sub_total(self):
        for z in self:
            z.sub_total = z.qty * z.harga_satuan
            
    @api.onchange('barang_id')
    def _onchange_(self):
        if self.barang_id.harga_jual:
            self.harga_satuan = self.barang_id.harga_jual
            
            
    @api.model
    def create(self, vals):
        record = super(dtrx, self).create(vals)
        if record.qty:
            self.env['h.barang'].search([('id', '=', record.barang_id.id)]).write({'stok' : record.barang_id.stok - record.qty})
        return record
    
    @api.constrains('qty')
    def cek_qty(self):
        for z in self:
            if z.qty < 1 : #z.name = false(?)
                raise ValidationError(f'{z.barang_id.name} belanja minimal 1 quantity, tidak boleh {z.qty}')
            elif z.barang_id.stok < z.qty :
                raise ValidationError(f'maaf, stok hanya tersedia {z.barang_id.stok}, kurang {z.qty - z.barang_id.stok} lagi')