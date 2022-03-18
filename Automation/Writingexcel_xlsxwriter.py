import xlsxwriter

workbook = xlsxwriter.Workbook("D:\\Resh JPDC\\Selenium_Python\\K_Notes\\DBfetching.xls")
worksheet = workbook.add_worksheet()

# Start from the first cell.
# Rows and columns are zero indexed.
row = 0
column = 0

content = ["ankit", "rahul", "priya", "harshita",
           "sumit", "neeraj", "shivam"]

# iterating through content list
for item in content:
    # write operation perform
    worksheet.write(row, column, item)

    # incrementing the value of row by one
    # with each iterations.
    row +=2

workbook.close()
