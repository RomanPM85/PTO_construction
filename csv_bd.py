import openpyxl
import csv

wb = openpyxl.load_workbook('BD-Materials.xlsx')
sh = wb.active # was .get_active_sheet()
with open('test.csv', 'w', newline="") as file_handle:
    csv_writer = csv.writer(file_handle)
    for row in sh.iter_rows(): # generator; was sh.rows
        csv_writer.writerow([cell.value for cell in row])
