import xlrd

#打开表格
def open_excel_file(filename,sheet_num=0):
    xlsfile = filename
    book = xlrd.open_workbook(xlsfile)
    sheet = book.sheet_by_index(sheet_num)
    na = book.sheet_names() #附表名字
    nrows = sheet.nrows    #行
    ncols = sheet.ncols    #列
    return sheet,nrows,ncols,na

#读取一列的数据
def read_excelNrows_file(filename,sheet_n,read_col = 0):
    sheet,nrows,ncols,sheet_name = open_excel_file(filename,sheet_num=sheet_n)
    data_list = []
    for i in range(nrows):
        data = sheet.cell_value(i,read_col)
        data_list.append(data)
    return data_list

#读取一行的数据
def read_excelNcols_files(filename,sheet_n,read_col = 0):
    sheet,nrows,ncols,sheet_name = open_excel_file(filename,sheet_num=sheet_n)
    data_list = []
    for i in range(ncols):
        data_list.append(sheet.cell_value(read_col,i))
    return data_list

if __name__ == '__main__':
    name = "D:\\Game\\JetBrains\\Ai-Link\\NB15\\NB15_data.xlsx"
    print(read_excelNcols_files(filename=name,sheet_n=0))
    print(read_excelNrows_file(filename=name,sheet_n=1))
