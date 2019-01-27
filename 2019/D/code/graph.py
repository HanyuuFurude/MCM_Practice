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
             #第一条边 第二条边 长度 容量
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
        return self.list[ID][3]-self.pathList[ID]

    def queryLength(self, ID):
        return self.list[ID][2]

    def setter(self, ID, val):
        self.pathList[ID] = val

    def getGraph(self):
        return self.list

    def avilable(self, a, b):
        for x in self.list:
            if [a, b] == [x[0], x[1]] or [a, b] == [x[1], x[0]]:
                return self.queryFree(x)
            else:
                return None


    def dijkstra(self, ID):
        n = len(self.graphNode)
        costs = {}
        parents = {}
        visited = {}
        for x in self.graphNode:
            costs[x] = float('inf')
            parents[x] = -1
            visited[x] = False
        costs[ID] = 0
        t = []
        while len(t) < n:
            minCost = float('inf')
            minNode = None
            for i in self.graphNode:
                if not visited[i] and costs[i] < minCost:
                    minCost = costs[i]
                    minNode = i
            t.append(minNode)
            visited[minNode] = True

            for edge in self.graphNode[minNode]:
                if self.avilable(edge,minNode):
                    if not visited[edge] and minCost + self.graphNode[minNode][edge] < costs[edge]:
                        costs[edge] = minCost + self.graphNode[minNode][edge]
                        parents[edge] = minNode
        self.path = ['Exit']
        node = parents['Exit']
        while node != -1:
            self.path.append(node)
            node = parents[node]
        return costs, parents, self.path


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

    a.setter('p000',50)
    print(a.queryFree('p000'))
    a.print()
