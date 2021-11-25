from openpyxl import load_workbook
from docx import Document
from docx.shared import Inches
wb = load_workbook(filename = 'C:\Table_to_word\Table_to_word\Михайлюцька ТГ.xlsx')
sheet_ranges = wb['Копія аркуша для акта інвентари']
print(sheet_ranges['A41'].value)

document = Document()

p = document.add_paragraph('A plain paragraph having some ')
#p.add_run('bold').bold = True
#p.add_run(' and some ')
#p.add_run('italic.').italic = True

#records = (
#    ((sheet_ranges['A41'].value), '101'),
#    (7, '422'),
#    (4, '631')
#)

#table = document.add_table(rows=26, cols=2)
#hdr_cells = table.rows[0].cells
#hdr_cells[0].text = 'Qty'
#hdr_cells[1].text = 'Id'
#hdr_cells[2].text = 'Desc'
#for qty, id, desc in records:
 #   row_cells = table.add_row().cells
  #  row_cells[0].text = str(qty)
   # row_cells[1].text = id
    #row_cells[2].text = desc
document.add_paragraph(sheet_ranges['A41'].value)
document.add_page_break()

document.save('demo.docx')