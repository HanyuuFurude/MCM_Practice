import reader

### 房间

# *   $roomID_i​$:房间唯一标识号
#
# *   $roomCapacity_i$:房间的容量(人)（由面积计算）
# *   $roomFloor_i$:房间所在的楼层数


class roomReader:
    def __init__(self, fileName='floor.xlsx'):
        readIn = reader.Reader(fileName)
        mat = readIn.getMartix()
        self.dic = {}
        for x in mat[0]:
            self.dic[str(int(x[1]))] = int(x[0])

    def query(self, s):
        if isinstance(s, str) is False:
            raise TypeError('str required,[Hanyuu]')
        else:
            return self.dic[s]


if __name__ == '__main__':
    s = roomReader('floor.xlsx')
    print(s.query('201'))
