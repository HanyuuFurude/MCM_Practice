# import room
import roomReader
import reader
from fs import fs
# from Dijkstra import dijkstra


class graph:
    def __init__(self):
        self.list = {}  # 图关系列表
        self.pathList = {}  # 路经运行时容量
        self.graphNode = {}

    def add(self, roomA, roomB, path):  # roomA/B为房间标识号，path为路经标识号
        self.list[path] = [roomA, roomB]

    def load(self):
        self.matrix = reader.Reader('data.xlsx').getMartix()[0]
        for x in self.matrix:
            self.graphNode[fs(x[1])] = {}
            self.graphNode[fs(x[2])] = {}

        for x in self.matrix:
            self.list[fs(x[0])] = [fs(x[1]), fs(x[2]), x[3], x[4]]
            self.pathList[fs(x[0])] = 0  # 初始化路表
            self.graphNode[fs(x[1])][fs(x[2])] = x[3]
            self.graphNode[fs(x[2])][fs(x[1])] = x[3]
    def print(self):
        for x in self.list:
            print('[edge]:', x, '[node]', self.list[x][0],
                  self.list[x][1], '[length]', self.list[x][2], '[capacity]', self.list[x][3], '\t[load]', self.pathList[x])

    def query(self, ID):
        return self.pathList[ID]
    def queryFree(self, ID):
        return self.list[ID][3]
    def queryLength(self,ID):
        return self.list[ID][2]

    def setter(self, ID, val):
        self.pathList[ID] = val
    def getGraph(self):
       return self.list
    def dijkstra(self, ID):
        pass



class roomList:
    def __init__(self):
        self.roomList = {}
        self.capacityList = {}
        self.loadList = {}
        self.reader = roomReader.roomReader()

    def load(self):
        self.matrix = reader.Reader('floor.xlsx').getMartix()[0]
        for x in self.matrix:
            self.roomList[fs(x[1])] = int(x[0])
            self.capacityList[fs(x[1])] = x[2]
            self.loadList[fs(x[1])] = 0

    def queryFree(self, ID):
        return self.capacityList[ID]-self.loadList[ID]

    def setter(self, ID, afford):
        self.loadList[ID] = afford

    def queryFloor(self, ID):
        return self.roomList[ID]

    def print(self):
        for x in self.roomList:
            print('[room]', self.roomList[x], '[capacity]',
                  self.capacityList[x], '\t[load]', self.loadList[x])




if __name__ == "__main__":
    a = graph()
    a.load()
    a.print()
    b = roomList()
    b.load()
    b.print()
    print(b.queryFree('173'))
    print(b.queryFloor('173'))
    b.setter('173', 40)
    print(b.queryFree('173'))
