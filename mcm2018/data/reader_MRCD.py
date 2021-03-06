class Reader:

    def __init__(self):
        self.fileName = '''data.xlsx'''
        self.filePath = os.path.dirname(os.path.abspath(__file__))
        print('[tips]请将数据文件'+self.fileName+"放在目录"+self.filePath+"下")
        print('[info] Start to load')
        import xlrd
        self.data = xlrd.open_workbook(self.filePath+'\\'+self.fileName)
        self.sheets = self.data.sheets()

    def print(self):
        for i in range(len(self.sheets)):
            print('\n[table' + str(i)+']\n'+self.sheets[i].name)
            for j in range(self.sheets[i].nrows):
                print(self.sheets[i].row_values(j))

    def getMartix(self):
        matrix = []
        for i in range(len(self.sheets)):
            subMat = []
            for j in range(self.sheets[i].nrows):
                subMat.append(self.sheets[i].row_values(j))
            matrix.append(subMat)
        return matrix

    def fileInfo(self):
        print('['+self.fileName+']'+' has '+str(len(mat))+' table(s)')
        for i in range(len(self.sheets)):
            print('\t[table '+str(i)+'] '+str(self.sheets[i].ncols) +
                  ','+str(self.sheets[i].nrows))


if __name__ == '__main__':
    import os
    print('[path] '+os.path.dirname(os.path.abspath(__file__)))
    reader = Reader()
    # reader.print()
    mat = reader.getMartix()
    reader.fileInfo()
