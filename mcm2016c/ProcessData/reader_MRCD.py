class Reader:

    def __init__(self):
        fileName = '''MRCD.xlsx'''
        filePath = os.path.dirname(os.path.abspath(__file__))
        print('[tips]请将数据文件'+fileName+"放在目录"+filePath+"下")
        print('[info] Start to load')
        import xlrd
        self.data = xlrd.open_workbook(filePath+'\\'+fileName)
        self.table = self.data.sheets()[0]

    def print(self):
        for i in range(self.table.nrows):
            print(self.table.row_values(i))

    def debug(self):
        print(self.table.ncols, self.table.nrows)
    
    def getMatrix(self):
        matrix = []
        for i in range(self.table.nrows):
            matrix.append(self.table.row_values(i))
        return matrix

    def getSubMatrix(self,*field):
        matrix = []
        for i in range(self.table.nrows):
            subMat = [] 
            for x in range(len(field)):
               subMat.append(self.table.cell(i,field[x]).value)
            matrix.append(subMat)
            del(subMat)
        return matrix


if __name__ == '__main__':
    import os
    print('[path] '+os.path.dirname(os.path.abspath(__file__)))
    reader = Reader()
    reader.debug()
    # reader.print()
    a = reader.getSubMatrix(5,6,7,8)
    print(type(a))
    print(a)

