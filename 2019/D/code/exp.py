import logMe
import roomReader
a = roomReader.roomReader()
print(a.query('201'))
b = logMe.logme()
b.log('log')
c = logMe.logme('hanyuu.log')
c.log('log')
