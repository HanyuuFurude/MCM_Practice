from reader import Reader
from fs import fs
# ### 人群
#
# *   $gID_i$:人群标识号
# *   $gSpeed_i$:群体速度
# *   $gPosition_i$:群体位置
# *   $gCount_i$:人群数
# *   $gDissociationProbability$:解离概率


class group:
    def __init__(self, uuid, position, count, port=None, por=0):
        self.gid = uuid
        self.gSpeed = 1.6
        self.gPosition = position
        self.gPositionOnRoad = por  # 若在路径上，记录当前行进距离
        self.gPositionOnRoadTo = port  # 若在路径上，记录目标容器
        self.gCount = count
        self.gDis = 0.05

    def load(self, graph):
        pass


class groupList:
    def __init__(self):
        self.matrix = Reader('data.xlsx').getMartix()[0]
        self.nodeList = {}
        self.newNodeList={}
        for x in self.matrix:
            for i in range(3):
                self.nodeList[fs(x[i])] = []
                self.newNodeList[fs(x[i])] = []
        self.matrix = Reader('floor.xlsx').getMartix()[0]
        for x in self.matrix:
            self.nodeList[fs(x[1])].append(group(0, fs(x[1]), int(x[3]))
                                                #uuid 房间号 人数
    def load(self, ID):
        sumUp = 0
        for x in self.nodeList[ID]:
            sumUp += x.gCount
        return sumUp


# 人

# *   $uuid_{i}$:人唯一标识号
#
# *   $speed_i$:速度
# *   $position$:位置（位于哪个个容器内）
# *   $positionOnRoad_i$:如果位于道路上，则记录在道路的位置（直接比照节点字符串值，小号为0起点）
# *   $psychologyValue_i$心理指标
# *   $t_i$:出逃时间

class person:
    def __init__(self, id):
        self.unid = id
        self.speed = 0
        self.position = 0
        self.pod = 0
        self.psy = 0.1
        self.time = 0


if __name__ == '__main__':
    a = groupList()
    pass
