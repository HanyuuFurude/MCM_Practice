### 非游客通道

# *   $uID_i$:非游客通道唯一标识号
# *   $uCapacity$:非游客通道容量

class staffPath:
    def __init__(self,id,cap):
        self.uid=id
        self.ucap=cap



### 道路

# *   $roadID_i​$:道路唯一标识号
# *   $roadCapacity_i$:道路容量（人）
# *   $roodNode​$:道路两端连接节点

class road:
    def __init__(self,id,cap,node):
        self.rid=id
        self.rcap=cap
        self.rNode=node


### 楼梯

# *   $stairID_i$:楼梯唯一标识号
# *   $stariCapacity$:楼梯容量
# *   $stairLength_i$:楼梯长度

class stair:
    def __init__(self,id,cap,len):
        self.sid=id
        self.scap=cap
        self.slen=len

