""" XLSX example

https://realpython.com/openpyxl-excel-spreadsheets-python/
"""
import openpyxl

wb = openpyxl.load_workbook('demo.xlsx')
sheet1 = wb['1. Quarter 2021']
cell = sheet1['B2']

print(cell)
print(cell.value)
