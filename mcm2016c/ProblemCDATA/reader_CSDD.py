import xlrd
import numpy as np


class Reader:

    def __init__(self):
        self.fileName = '''CSDD.xlsx'''
        self.filePath = os.path.dirname(os.path.abspath(__file__))
        print('[tips]请将数据文件'+self.fileName+"放在目录"+self.filePath+"下")
        print('[info] Start to load')
        self.data = xlrd.open_workbook(self.filePath+'\\'+self.fileName)
        self.table = self.data.sheets()[0]
        self.dataMartix = np.zeros((self.table.nrows, self.table.ncols))
        # for x in range(self.table.ncols):
        #     col = self.table.col_values(x)
        #     col = np.matrix(col)
        #     self.dataMartix[:, x] = col

    def print(self):
        for i in range(self.table.nrows):
            print(self.table.row_values(i))

    def debug(self):
        print(self.table.cell(17, 0).value)
        print(self.dataMartix[17][0])
        print(type(self.table))
        print(type(self.table.cell(0, 0)))
        print(type(self.dataMartix))
        print(self.table.nrows, self.table.ncols)
        f = open(self.filePath+'\\Hanyuu.log', 'w')
        for x in range(self.table.nrows):
            if(self.table.cell(x, 0).value != ''):
                print(self.table.cell(x, 0).value)
                f.write(self.table.cell(x, 0).value+'\n')
        f.close()


if __name__ == '__main__':
    import os
    print('[path] '+os.path.dirname(os.path.abspath(__file__)))
    reader = Reader()
    # reader.print()
    reader.debug()
