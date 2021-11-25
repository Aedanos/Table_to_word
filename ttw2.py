from openpyxl import load_workbook
from docx import Document
from docx.shared import Inches

wb = load_workbook(filename = 'C:\Table_to_word\Table_to_word\Михайлюцька ТГ.xlsx')
sheet = wb.active
sheet_ranges = wb['Копія аркуша для акта інвент(2)']
print(sheet_ranges['A41'].value)

document = Document()

for i in range(9):
    document.add_table(rows=2, cols=2)
    document.add_paragraph('')

table = document.add_table(rows=2, cols=2)
document.add_page_break()

table[і].cell (0,0) .text = sheet_ranges['A42'].value
table.cell (1,0) .text = sheet_ranges['A42'].value

table.cell (0,1) .text = sheet_ranges['B41'].value
table.cell (1,1) .text = sheet_ranges['B42'].value

        
document.add_page_break()

document.add_paragraph(sheet_ranges['A41'].value)

document.add_page_break()

document.save('demo.docx')