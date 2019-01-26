import room
import roomReader
import reader


class graph:
    def __init__(self):
        self.list = {}

    def add(self, roomA, roomB, path):  # roomA/B为房间标识号，path为路经标识号
        self.list[path] = [roomA, roomB]

    def load(self):
        self.matrix = reader.Reader('data.xlsx').getMartix()[0]
        for x in self.matrix:
            self.list[x[0]] = [x[1], x[2], x[3], x[4]]

    def print(self):
        for x in self.list:
            print('[edge]:', x, '[node]', self.list[x][0], self.list[x][1])


class roomList:
    def __init__(self):
        self.roomList = {}
        self.reader = roomReader.roomReader()

    def add(self, ID, capacity):
        res = room.room(ID, capacity, self.reader.query(ID))
        self.roomList[ID] = [res, 0]  # 后一个参数为载荷

    def query(self, ID):
        return self.roomList[ID][1]

    def setter(self, ID, afford):
        self.roomList[ID][1] = afford

    class path:
        def __init__(self):
            pass


if __name__ == "__main__":
    a = graph()
    a.load()
    a.print()
    b = roomList()
    b.add('100', 500)
    print(b.query('100'))
    b.setter('100', 40)
    print(b.query('100'))
