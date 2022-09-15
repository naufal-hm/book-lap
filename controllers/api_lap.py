from odoo import http
from odoo.http import request
import json


class apilap(http.Controller):
    @http.route('/hapis/lapangan', method=['GET'], auth='public')
    def apilap(self, **kw):
        lapangan = request.env['h.lapangan'].search([])
        deta = []
        for z in lapangan:
            deta.append({
                'id lapangan': z.id_lapangan,
                'tipe lapangan' : z.jenis_lap,
                'harga lapangan' : z.harga_lap,
                'jenis lapangan' : z.jenislapangan_id.name,
                'waktu kosong' : z.waktu_kosong
            })
        return json.dumps(deta)
