import xlwt 
from xlwt import Workbook 
  
# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 
  
sheet1.write(1, 0, '') 
sheet1.write(2, 0, '') 
sheet1.write(3, 0, '') 
sheet1.write(4, 0, '') 
sheet1.write(5, 0, '') 
sheet1.write(0, 1, '') 
sheet1.write(0, 2, '') 
sheet1.write(0, 3, '') 
sheet1.write(0, 4, '') 
sheet1.write(0, 5, '') 
  
wb.save('xlwt example.xls') 
