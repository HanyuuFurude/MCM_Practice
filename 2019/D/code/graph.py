# import room
import Global
import roomReader
import reader
import people
from fs import fs
from disaster import disaster
import logMe
# from Dijkstra import dijkstra


class graph:
    def __init__(self):
        self.list = {}  # 图关系列表
        # self.pathList = {}  # 路经运行时容量
        self.graphNode = {}
        self.load()

    def add(self, roomA, roomB, path):  # roomA/B为房间标识号，path为路经标识号
        self.list[path] = [roomA, roomB]

    def load(self):
        self.matrix = reader.Reader('data.xlsx').getMartix()[0]
        for x in self.matrix:
            self.graphNode[fs(x[1])] = {}
            self.graphNode[fs(x[2])] = {}

        for x in self.matrix:
            self.list[fs(x[0])] = [fs(x[1]), fs(x[2]), x[3], x[4]]
            # 第一条边 第二条边 长度 容量
            # self.pathList[fs(x[0])] = 0  # 初始化路表
            self.graphNode[fs(x[1])][fs(x[2])] = x[3]
            self.graphNode[fs(x[2])][fs(x[1])] = x[3]

    # def print(self):
    #     for x in self.list:
    #         print('[edge]:', x, '[node]', self.list[x][0],
    #               self.list[x][1], '[length]', self.list[x][2], '[capacity]', self.list[x][3], '\t[load]', self.pathList[x])

    # def query(self, ID):
    #     return self.pathList[ID]

    # def queryFree(self, ID):
    #     return self.list[ID][3]-self.pathList[ID]

    def queryLength(self, ID):
        return self.list[ID][2]

    # def setter(self, ID, val):
    #     self.pathList[ID] = val

    def getGraph(self):
        return self.list

    # def avilable(self, a, b):  # 两点之间的路径的容量
    #     for x in self.list:
    #         if [a, b] == [self.list[x][0], self.list[x][1]] or [a, b] == [self.list[x][1], self.list[x][0]]:
    #             return self.queryFree(x)
    #     return None

    def getPathID(self, a, b):  # 两点之间的路径的标识符
        for x in self.list:
            if [a, b] == [self.list[x][0], self.list[x][1]] or [a, b] == [self.list[x][1], self.list[x][0]]:
                return x
        return None

    def freeCapacity(self, ID=None, g=None):  # 查询边的剩余容量
        return self.list[ID][3] - g.load(ID)

    def dijkstra(self, ID, g):
        if ID == 'Exit':
            return [['Exit'], float('inf')]
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
                if self.freeCapacity(self.getPathID(edge, minNode), g) > 0:
                    if not visited[edge] and minCost + self.graphNode[minNode][edge] < costs[edge]:
                        costs[edge] = minCost + self.graphNode[minNode][edge]
                        parents[edge] = minNode
        self.path = ['Exit']
        node = parents['Exit']
        while node != -1:
            self.path.append(node)
            node = parents[node]
        route = float('inf')

        if ID in self.path:
            for x in range(len(self.path)):
                if x == len(self.path)-1:
                    break
                temp = self.freeCapacity(self.getPathID(
                    self.path[x], self.path[x+1]), g)
                if temp < route:
                    route = temp
        else:
            route = 0
        # return costs, parents, self.path
        return [self.path, route]


class roomList:
    def __init__(self):
        self.roomList = {}
        self.capacityList = {}
        self.loadList = {}
        self.reader = roomReader.roomReader()
        self.load()

    def load(self):
        self.matrix = reader.Reader('floor.xlsx').getMartix()[0]
        for x in self.matrix:
            self.roomList[fs(x[1])] = int(x[0])
            self.capacityList[fs(x[1])] = x[2]
            self.loadList[fs(x[1])] = 0

    def queryFree(self, ID):
        return self.capacityList[ID] - self.loadList[ID]

    def queryLoad(self, ID):
        return self.loadList[ID]

    def setter(self, ID, afford):
        self.loadList[ID] = afford

    def queryFloor(self, ID):
        return self.roomList[ID]

    def print(self):
        for x in self.roomList:
            print('[room]', self.roomList[x], '[capacity]',
                  self.capacityList[x], '\t[load]', self.loadList[x])


def sumCount(val):
    Global.score += Global.clockCount * Global.SECOND_PER_FRAME + val
    Global.savedPopulation += val


# if __name__ == "__main__":
#     a = graph()
#     b = roomList()
#     c = people.groupList()
#     for listn in c.nodeList:
#         for x in c.nodeList[listn]:
#             b.setter(x.gPosition,x.gCount)

#     while Global.savedPopulation < 14717 and Global.clockCount < 1080:
#         Global.clockCount+=1
#         for listn in c.nodeList:
#             for x in c.nodeList[listn]:
#                 if listn[0] != 'p':  # 在房间或楼梯内
#                     if x.gPosition == 'Exit':  # 完事溜了
#                             sum(x.gCount)
#                             b.setter(x.gPosition, b.queryLoad(x.gPosition) - x.gCount)  # 负荷转移
#                             del x
#                             continue
#                     [pathn, countn] = a.dijkstra(x.gPosition)
#                     while (x.gPosition in pathn):
#                         newNode = people.group(
#                             x.gid, pathn[-2], min(x.gCount, countn))

#                         newNode.gPosition = a.getPathID(pathn[-1], pathn[-2])
#                         newNode.gPositionOnRoad = 0
#                         newNode.gPositionOnRoadTo = pathn[-2]
#                         c.nodeList[a.getPathID(pathn[-1], pathn[-2])].append(newNode)  # 送到路径上
#                         x.gCount -= min(x.gCount, countn)
#                         b.setter(pathn[-1], b.queryLoad(pathn[-1]) -
#                                  min(x.gCount, countn))  # 负荷转移
#                         b.setter(pathn[-2], b.queryLoad(pathn[-2]) +
#                                  min(x.gCount, countn))
#                         if x.gCount == 0:
#                             del x
#                             break
#                 else:
#                     x.gPositionOnRoad += x.gSpeed * Global.SECOND_PER_FRAME
#                     if x.gPositionOnRoad >= a.queryLength(x.gPosition):
#                         if x.gPositionOnRoadTo == 'Exit':  # 完事溜了
#                             sum(x.gCount)
#                             # 负荷转移
#                             a.pathList[x.gPosition] = a.pathList[x.gPosition] - x.gCount
#                             del x
#                             continue
#                         a.pathList[x.gPosition] = a.pathList[x.gPosition] - x.gCount  # 负荷转移
#                         b.setter(x.gPositionOnRoadTo, b.queryLoad(
#                             x.gPositionOnRoadTo) + x.gCount)
#     print('[score]:', Global.score)
#     print('[Saved]:', Global.savedPopulation)

#     pass
if __name__ == '__main__':
    # 初始化
    gr = graph()
    r = roomList()
    g = people.groupList()
    countLog = logMe.logme('HanyuulogCount.log')
    snapLog = logMe.logme('HanyuulogSnap.log')
    # 主循环
    while Global.clockCount < 1000:
        # 时钟计数
        Global.clockCount += 1
        # 时钟日志
        print(Global.clockCount)
        # 切片日志
        if Global.clockCount % 3 == 0:
            countLog.log(Global.clockCount,
                         Global.savedPopulation, Global.score)
            for x in g.nodeList:
                snapLog.log(x, g.load(x))
            snapLog.log('')
        # 演算
        # 遍历所有容器
        for x in g.nodeList:
            # 遍历该容器下的所有group
            for i in g.nodeList[x]:
                # 楼梯和房间
                if i.gPosition[0] != 'p':
                    # 在出口，直接溜
                    if x == 'Exit':
                        sumCount(i.gCount)
                        del i
                        continue
                    # 向前找路
                    else:
                        # 带时间窗的寻路
                        res = gr.dijkstra(x, g)
                        # 当前节点分流
                        while i.gCount > 0:
                            new = people.group(0, gr.getPathID(
                                res[0][-2], i.gPosition), min(res[1], i.gCount), res[0][-2])
                            # 占领时间窗
                            g.newNodeList[new.gPosition].append(new)
                            i.gCount -= min(res[1], i.gCount)
                            if i.gCount == 0:
                                break
                            # 路径迷失
                            elif i.gPosition in res[0] is False:
                                g.newNodeList[i.gPosition].append(i)
                                break
                # 道路
                else:
                    i.gPositionOnRoad += i.gSpeed * Global.SECOND_PER_FRAME
                    if i.gPositionOnRoad > gr.list[i.gPosition][2]:
                        new = people.group(0, i.gPositionOnRoadTo, i.gCount)
                        g.newNodeList[i.gPositionOnRoadTo].append(new)
        # 新旧交替
        for x in g.newNodeList:
            g.nodeList[x].clear()
            if x[0] != 'p':
                sum = 0
                for i in g.newNodeList[x]:
                    sum += i.gCount
                if sum > 0:
                    g.nodeList[x].append(people.group(0, x, sum))
            else:
                for i in g.newNodeList[x]:
                    g.nodeList[x].append(i)
            g.newNodeList[x].clear()
