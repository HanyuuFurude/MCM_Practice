class logme:
    def __init__(self, fileName='log.log'):
        self.fileName = fileName

    def log(self, txt):
        with open(self.fileName, 'a+') as l:
            l.write(txt)
