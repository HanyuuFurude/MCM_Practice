# 概述

行车问题

在宏观上而言在空间上是车辆是离散的，时间上可以看作是离散的（对时间细粒度不敏感），道路的状态也是离散的（对道路细粒度不敏感）；在微观上而言，对于每一个车辆来说，他们只需关心自己和自己周围有限的对象（其他车辆，道路等）即可做出判断 ，由于道路问题在车流量变更在有限范围内的时候可以看作是周期性或者混沌型，由此可以对指定交通规则下指定负荷条件下的道路运输情况做出定量评估，我们将模型以元胞机的变种定义并运行模拟，该系统为道路交通中有关秩序、紊动 、混沌 、非对称、分形等系统整体行为与复杂现象的研究提供了一个有效的模型工具，通过对各种情况进行的模拟，（这边结论瞎蒙的）我们发现靠右行车靠左超车的模式在普通负载以人类驾驶员为主的道路上相对较高，效率使用率达到40%，低负载下使用相对合理在但是高负载下会直接造成近80%的占空率，安全性一般，然而对于通过一定算法安排的控制体系来说，该规则浪费空间现象较为严重，表现仅为，针对无中心的控制体系，我们使用……规则将占用率进化到了……同时保证安全性

# Tips

下面出现的所有常数性常量我都没有查过鹰酱的国情emmm……这个得麻烦你慢慢查+引用收集了emmm……

# assumption

* 在车道上运行的车有两种，一种是运送货物的，一种是搭载乘客的
* 在城区行驶的车辆都是小型轿车，在rural行驶都是大型客车和货车

# limits

我们对行驶在高速公路上的车辆建立一个宏观模型，在这个模型中有如下限制：安全的跟车距离、车辆的最高速度和车道数。因为美国各州的交通规则都不尽相同，Figure1，例如On rural [Interstate Highways](https://en.wikipedia.org/wiki/Interstate_Highway_System) and other [freeways](https://en.wikipedia.org/wiki/Controlled-access_highway), the speed limit ranges from 60 mph (96 km/h) in Hawaii to 85 mph (136 km/h) in parts of [Texas](https://en.wikipedia.org/wiki/Texas). 因此，我们选取Arizona州作为样例进行分析。根据Arizona州政府交通网站的数据，在高速公路行驶的车辆应当与前车保持安全的距离，这个距离与车速有关。当车速超过100km/h时，应当与同车道的前车保持100m以上的距离；车速低于100/h的时候，可以与前车适当缩短距离，但是最小距离不得少于50m。同样是Arizona州，在urban高速公路上行驶的限速从89km/h到105km/h，rural从105km/h到121km/h，车道数量有两车道、四车道（单向）即双向一共4、8条车道。

![](F:\github\MCM_Practice\mcm2014\220px-US_Speed_Limits_May_2015.svg.png)



* 安全跟车距离

    * 根据《中华人民共和国道路交通安全法实施条例》第八十条，机动车在高速公路上行驶，车速超过每小时100公里时，应当与同车道前车保持100米以上的距离，车速低于每小时100公里时，与同车道前车距离可以适当缩短，但最小距离不得少于50米。

    * 没找到老美的，都是单纯的说一句保持距离。。。不过可以编一句，根据Arizona的政府数据。["Driving Tips & Rules for Easy Car Rental in USA"](http://www.usacarsrental.com/useful-stuff/). *Usacarsrental.com*. Retrieved 2017-07-27.

* 车辆限速

    * //TODO:不同车型的限速（轿车120，客运+货车100，这个是兔子的，到时候改成老美的），老美日常国情出处同上
    * On rural [Interstate Highways](https://en.wikipedia.org/wiki/Interstate_Highway_System) and other [freeways](https://en.wikipedia.org/wiki/Controlled-access_highway), the speed limit ranges from 60 mph (96 km/h) in Hawaii to 85 mph (136 km/h) in parts of [Texas](https://en.wikipedia.org/wiki/Texas). 从维基百科（Wikipedia）抄来的（文件夹中附图）
    * 这里我们采用Arizona州的数据，Freeway（rural）是105-121km/h，Freeway（urban）是89-105km/h。数据来源是Arizona Statutes Chapter 3 Article 6 [State Legislature](http://www.azleg.state.az.us/ArizonaRevisedStatutes.asp?Title=28%7CArizona)

* 车道数

    * 变量，一般情况下为2，包含一个行车道一个超车道，根据老美国情（资料+引用）可增配至（双向）四、六车道
    * [Overtaking](https://en.wikipedia.org/wiki/Overtaking), usually called "passing", is legal on all four or more lane roads and on most two-lane roads with sufficient sight distance. 
    * *来源：Department of Transportation*. State of California. from the original on March 24, 2012. Retrieved June 3, 2013.
    * 车道容量（Capacity）：Lane capacity varies widely due to conditions such as neighboring lanes, lane width, elements next to the road, number of driveways, presence of parking, speed limits, number of heavy vehicles and so on – the range can be as low as 1000 passenger cars / hour to as high as 4800 passenger cars / hour but mostly falls between 1500 and 2400 passenger cars / hour.
    * *车道容量的来源：Guide to Traffic Management Part 3: Traffic Studies and Analysis*. [Austroads](https://en.wikipedia.org/wiki/Austroads). 2013. pp. Section 4.

# 评价指标

为The Keep-Right-Except-To-Pass Rule 模型建立一个评价指标等价运输量，用于描述该模型的traffic flow。假设在路上行驶的车辆有两种，分别是运送货物的和搭载乘客的，总的等价运量等于客流量加物流量。但是因为客流量的单位是人，物品运输的单位是吨，所以这里涉及一个单位换算的问题。...............



* 等价运量
  * 客流量 计量单位：吨
  * 物流量 计量单位：人次
  * 根据物流每吨公里价和一般客车的人均公里价换算，统一成吨比较好？（讨论点）
# （伪）元胞参数

## 单个车辆

在宏观上而言在空间上是车辆是离散的，时间上可以看作是离散的（对时间细粒度不敏感），道路的状态也是离散的（对道路细粒度不敏感）；在微观上而言，对于每一个车辆来说，他们只需关心自己和自己周围有限的对象（其他车辆，道路等）即可做出判断 ,因此可以用元胞模型的变异来描述时间和空间上离散的车流，这里我们将每辆车看成一个元胞。每一个元胞都有如下参数：

|           |                                         |
| --------- | --------------------------------------- |
| speed     | speed of a car                          |
| length    | length of a car                         |
| size      | type of a car (0:轿车 1：大型客车/货车) |
| capcity   | equivalent load                         |
| MAX_SPEED | maximun speed                           |
| prior     | priority                                |

![](F:\github\MCM_Practice\mcm2014\car.jpg)

* 



``` py
	def __init__(self):
		self.speed = 0	# m/s
		self.length = 0	# m
		self.size = None # 车型 [0:桥车 1：大客、货运]（影响限速）
		self.capcity = 0	#等效载荷（客运；人/货运：吨）（载荷由公式给出）
		self.MAX_SPEED =0#最大速度 m/s
		self.prior = 5 # 优先级
```
代码贴这里了你描述一下有哪些参数画一下参数约定表

## 两辆车之间

![](F:\github\MCM_Practice\mcm2014\overtaking.jpg)

两车之间存在速度差，以及相对距离。

# 模型计算

//TODO:占坑明天我做，东西比较多我困了让我先想一晚上

# 特殊情况



* 交通阻塞环（学名叫啥忘了emmm……）（通过模拟应当出现此效果）
    * 解决方案，人类驾驶约定堵塞时将自己的车控制在前后两车的中点上（啥地方看到的解决方案2333，到时候贴数据证明）
    * 统一控制就没这种问题了
* 侵限与事故
    * 划定车辆前端单车道（公式计算）为阻塞区禁止侵限区内出现其他车辆或异物，若出现就最大ABS要么停下来等前车开走要么boom，事故区约定一段时间的事故处理时间并做临时固定阻塞区模拟正式环境下的事故处理
* 车道占用率问题
    * 计算车辆总长度比上道路总长度，可以结合速度计算负荷效率
* 连续变道
    * 连续变道在人类驾驶情况下是禁止的（文献引用）
    * 同一控制下不存在这个问题
* 变道过程与变道动作中的侵限判定（有空考虑视野问题）
    * 变道时阻塞区将扩展到原车道和待转入车道直至变道动作完成（有一段时间，这段时间会急剧增大阻塞面积并堵塞多个车道）
* 弯道
    * 减速区（易造成堵塞环和堵塞）
* 匝道
    * 高速出入口（效率高的时候匝道也会成为瓶颈造成堵塞，但是没有堵塞环了（都开完了））
* 分岔口
    * 减速+车道选择（必须为有意识的提前选择车道）
* 环道
    * //还没想明白，可以不上，模拟的是绕城高速的情况
# 讨论情况
* 车流量负荷
    * 高负荷时……
    * 中等负荷时……
    * 低负荷时……
    * 依靠不同的发车概率加载负荷
* 车速分布
    * 车速均匀、方差小，超车现象少、影响因素小
    * 车速不均匀、方差大、超车现象多，影响因素大
* 左/右舵交换
    * 讲道理只不过时镜像问题，肯定没问题的
* 人工驾驶风格/智能控制系统风格（独立执行/中央统一调配）
    * 这个直接元胞机？说法我写吧
* 安全系数
    * 事故率
* 提出新规则
    * 我编

# 敏感度分析

*   直接通过给单个参数+/- 步长看敏感性

# 误差分析

*   拟合车流数据（去鹰酱高速路政那边看看）

# 总公式

## 显然现在写的这些公式是很粗糙很有问题的，后面我来改就完事了

（P。S。真的不考虑 LaTex了嘛~）

平均：
$$Trans = \frac{\sum capicity_i(in\quad time\quad t \quad and  \quad distance \quad v*t)}{t}$$
瞬时：
$$dTrans = \frac{\sum capicity_i(通过截面)}{v}$$

