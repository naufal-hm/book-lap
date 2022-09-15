from odoo import models
from datetime import datetime


class PartnerXlsx(models.AbstractModel):
    _name = 'report.halosport.report_h_trx'
    _inherit = 'report.report_xlsx.abstract'
    waktu = datetime.now().strftime("%a, %d-%m-%y %I:%M %p")


    def generate_xlsx_report(self, workbook, data, partners):
        #nama sheet
        sheet = workbook.add_worksheet('historyy transaksi')
        bold = workbook.add_format({'bold': True})
        sheet.write(0,0, self.waktu)
        row = 1
        col = 0
        for z in partners:
            if z.name.name:
                sheet.write(row, 0, z.name.name, bold)
            else: sheet.write(row, 0, z.non_member, bold)
            sheet.write(row, 1, str(z.waktu) + str(' jam'))
            sheet.write(row, 2, z.lapangan_id.name)
            # sheet.write(row, 3, z.detailtrx_ids.barang_id.name)

            rowo = row
            rudo = 0
            for x in z.detailtrx_ids.barang_id:
                if rudo == len(z.detailtrx_ids) // 2 :
                    sheet.write(rowo, col+4, x.name)
                    rowo += 1
                else:
                    sheet.write(row, col+3, x.name)
                    rudo += 1
                    row += 1

            row += 1

        