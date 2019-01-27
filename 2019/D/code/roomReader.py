import reader

### 房间

# *   $roomID_i​$:房间唯一标识号
#
# *   $roomCapacity_i$:房间的容量(人)（由面积计算）
# *   $roomFloor_i$:房间所在的楼层数


from fs import fs
class roomReader:
    def __init__(self, fileName='floor.xlsx'):
        readIn = reader.Reader(fileName)
        mat = readIn.getMartix()
        self.dic = {}
        self.capacity={}
        for x in mat[0]:
            self.dic[fs(x[1])] = int(x[0])
            self.capacity[fs(x[1])]=x[2]

    def query(self, s):
        if isinstance(s, str) is False:
            raise TypeError('str required,[Hanyuu]')
        else:
            return self.dic[s]
    def queryCapacity(self,s):
        return self.capacity[s]


if __name__ == '__main__':
    s = roomReader('floor.xlsx')
    print(s.query('201'))
    print(s.queryCapacity('201'))
