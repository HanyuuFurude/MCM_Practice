### Summary

安防问题在当今时代

## 参数表

### 度量衡:SI

### 全局

*   $SECOND\_PER\_FRAME$:每帧秒数
*   $clockCount$:时钟计数
*   $savedPopulation$:出逃人数
*   $score$:评估分

### 房间

*   $roomID_i​$:房间唯一标识号

*   $roomCapacity_i$:房间的容量(人)（由面积计算）
*   $roomFloor_i$:房间所在的楼层数

### 道路

*   $roadID_i​$:道路唯一标识号
*   $roadCapacity_i$:道路容量（人）
*   $roodNode​$:道路两端连接节点

### 楼梯

*   $stairID_i$:楼梯唯一标识号
*   $stariCapacity$:楼梯容量
*   $stairLength_i$:楼梯长度

### 人

*   $uuid_{i}$:人唯一标识号

*   $speed_i$:速度
*   $position$:位置（位于哪个个容器内）
*   $positionOnRoad_i$:如果位于道路上，则记录在道路的位置（直接比照节点字符串值，小号为0起点）
*   $psychologyValue_i$心理指标
*   $t_i$:出逃时间

### 人群

*   $gID_i$:人群标识号
*   $gSpeed_i$:群体速度
*   $gPosition_i$:群体位置
*   $gCount_i$:人群数
*   $gDissociationProbability$:解离概率

### 灾害

*   $dCase$:灾害类型
*   $dPosition$:灾害原生发生位置
*   $dTrend$:灾害流动趋势

### 非游客通道

*   $uID_i$:非游客通道唯一标识号
*   $uCapacity$:非游客通道容量



## 评估公式

我们考虑了三种评估公式

1.  将最后一个人的逃出时间作为评估模型的度量值

    $$score=t_i,(i=max(t_i))$$	

    *   优点：能优化最后一个人的出逃时间，增加了无伤亡情况的可能性
    *   缺点：
        1.  不能让总体人员在尽可能短的时间内出逃
        2.  可能有人员会陷入断路而无法逃出的情况，此时无法统计

2.  $$score=\sum_{i}t_i$$

    *   优点：能兼顾逃生的整体时间
    *   缺点：
        1.  不能保证无伤亡的可能性尽可能小
        2.  在不同的时间$t$单位时间的价值$\Delta t$不等

3.  $$score=\sum_{i}(t_{i})^k$$

    *   优点：
        1.  考虑了不同的时间$t$单位时间的价值$\Delta t$不等
        2.  能将综合损失降低到最小
    *   缺点：无法直接提升无伤亡情况的可能性

