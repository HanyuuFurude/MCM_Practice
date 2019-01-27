class logme:
    def __init__(self, fileName='log.log'):
        self.fileName = fileName

    def log(self, *txt):
        with open(self.fileName, 'a+') as l:
            sum=''
            for x in txt:
                sum += str(x) + '\t'
            l.write(sum)
if __name__ == '__main__':
    a = logme()
    a.log('a',1,3)
