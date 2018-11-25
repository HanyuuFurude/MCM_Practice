class Reader:

    def __init__(self):
        fileName = '''IPEDS_UID.xlsx'''
        filePath = os.path.dirname(os.path.abspath(__file__))
        print('[tips]请将数据文件'+fileName+"放在目录"+filePath+"下")
        print('[info] Start to load')
        import xlrd
        data = xlrd.open_workbook(filePath+'\\'+fileName)
        table = data.sheets()[0]
        for i in range(table.nrows):
            print(table.row_values(i))


if __name__ == '__main__':
    import os
    print('[path] '+os.path.dirname(os.path.abspath(__file__)))
    reader = Reader()
    reader.__init__
