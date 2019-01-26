# ### 人群
#
# *   $gID_i$:人群标识号
# *   $gSpeed_i$:群体速度
# *   $gPosition_i$:群体位置
# *   $gCount_i$:人群数
# *   $gDissociationProbability$:解离概率
class people:
    def __init__(self,unid):
        self.gid=unid
        self.gSpeed=0
        self.gPosition=0
        self.gCount=0
        self.gDis=0



### 人

# *   $uuid_{i}$:人唯一标识号
#
# *   $speed_i$:速度
# *   $position$:位置（位于哪个个容器内）
# *   $positionOnRoad_i$:如果位于道路上，则记录在道路的位置（直接比照节点字符串值，小号为0起点）
# *   $psychologyValue_i$心理指标
# *   $t_i$:出逃时间

class person:
    def __init__(self,id):
        self.unid=id
        self.speed=0
        self.position=0
        self.pod=0
        self.psy=0.1
        self.time=0