import threading
import time
import math
import re
import random

SECONDS_PER_CLOCK = 5  # 时钟时间数
JUM_PROCESS_CLOCK = 1000  # 事故处理时钟数


class Car:
    uuid = 0

    def __init__(self):
        self.uuid = Car.uuid  # 车辆识别码，若识别码为负表示是障碍
        Car.uuid += 1  # 生成新的uuid
        self.speed = 0  # m/s
        self.length = 0  # m
        self.size = None  # 车型 [0:桥车 1：大客、货运]（影响限速）
        self.capacity = 0  # 等效载荷（客运；人/货运：吨）（载荷由公式给出）（为障碍时复用做计数器）
        self.MAX_SPEED = 0  # 最大速度 m/s
        self.aacc = 0  # 加速度
        self.dacc = 0  # 刹车加速度
        self.prior = 5  # 优先级
        self.position = 0  # 里程
        self.lane = 0  # 行驶车道（0，行车道 >=1的整数，一位奇数小数，从低号向高号道变道3 5 7 9，一位偶数小数，从高号到低号变道2 4 6 8）

    # self.roadDelta = []  # 当前占用的路段微元

    def saftyDistence(self):  # 安全跟车距离 m
        if (self.speed >= 100):
            return 100
        elif (self.speed >= 50):
            return self.speed
        elif (self.speed >= 10):
            return 50
        else:
            return 5

    def saftyFront(self):  # 安全跟车前限 m
        return self.position + self.length + self.saftyDistence()

    def confilct(self, car):  # 合并车道侵限判定（不考虑车道）
        if self.position > car.saftyFront():
            return False  # 无冲突，车辆在后方
        elif self.saftyDistence() < car.position:
            return False  # 无冲突，车辆在前方

    def load(self, length=0, size=None, capacity=0, MAX_SPEED=0, aacc=0, dacc=0, prior=0, position=0, lane=0,
             isCar=True, ):
        self.length = length
        self.size = size
        self.capacity = capacity
        self.MAX_SPEED = MAX_SPEED
        self.aacc = aacc
        self.dacc = dacc
        self.prior = prior
        self.position = position
        self.lane = lane
        if not isCar:
            self.uuid = -self.uuid  # 标记为路障

    def speedConv(self):  # 码制转换
        return self.speed * 3.6


def n2si(speed):  # km/h to m/s
    return speed / 3.6


def si2n(speed):  # m/s to km/h
    return speed * 3.6

# def update(self):
# 	pass


#   效率低下，舍弃
# class roadDelta:    # 路段微元
# 	def __init__(self,mileage, length = None ,speedLimit = None,laneCount = None,next = None):
# 		self.mileage = mileage #里程数
# 		self.length = length    #微元长度
# 		self.speedLimit = speedLimit    #区间限速
# 		self.laneCount = laneCount  #车道数
# 		self.catList = []   #当前占用该路段微元的车辆列表（事故区域算速度为0在特定时间存在的的特殊“车辆”）
# 		self.next = next    #下一微元链接
#
#
class Road:  # 道路

    def __init__(self, length):
        self.length = length
        self.carList = []  # 当前占用该路段微元的车辆列表（事故区域算速度为0在特定时间存在的的特殊“车辆”）挂载车辆尾部
        self.laneList = []  # 道路上车道情况列表，第一参数表示里程，第二参数表示车道数
        self.speedLimits = []  # 特殊路段限速，第一参数表示车型，第二参数表示限速

    def addCar(self, car):  # 从起点加载一辆新车
        self.carList.append(car)

    def crash(self, carList):  # 事故处理
        begin = carList[0]  # 保存头车
        begin.uuid = -abs(begin.uuid)  # 标记为路障（事故区域）
        begin.speed = 0  # 速度清零
        begin.capacity = 0  # 计数器清零
        begin.length = 0  # 长度清零在下面计算事故路段长度
        for x in carList:
            begin.length += x.length
            self.carList.remove(x)
        self.carList.append(begin)

    def laneCount(self, position):  # 计算给出坐标系下车道数
        res = 0
        for x in self.laneList:
            if x[0] > position:
                return res
            res = x[1]
        return self.laneList[0][1]

    def speedLimit(self, position):
        res = 0
        for x in self.speedLimits:
            if x[0] > position:
                return res
            res = x[1]
        return self.speedLimits[0][1]

    #
    # for x in range(len(carList)-1):
    # 	for y in self.carList:
    # 		if (y[1].uuid == x.uuid):
    # 			self.carList.remove(y)
    def update(self):
        flag = False  # false:无侵限，保持速度或加速
        # 调整速度和变道策略
        for x in self.carList:
            for i in self.carList:
                if not x.confilct(i):  # 无侵限，过滤
                    continue
                elif x.position >= i.position:  # 后车侵限
                    continue
                else:  # 前车/障碍侵限
                    flag = True
                    if self.laneCount(x) > x.lane:  # 未在最高速道上
                        for j in self.carList:
                            if math.floor(j.lane) == x.lane + 1:  # 已经考虑了变道中的车辆的双占用
                                if x.confilct(j):  # 不允许变道，制动
                                    x.speed -= x.dacc * SECONDS_PER_CLOCK  # 制动
                                    if x.speed < 0:
                                        x.speed = 0
                                    flag = True
                                    break
                        x.lane += 0.3  # 直接变道
                        flag = True
                        break
                    else:  # 在最高速道上，直接制动
                        x.speed -= x.dacc * SECONDS_PER_CLOCK  # 制动
                        if x.speed < 0:
                            x.speed = 0
                        flag = True
                        break
            if not flag:  # 正常0
                if (float(x.speed) < float(self.speedLimit(x.position))) and (float(x.speed) < float(x.MAX_SPEED)):
                    x.speed += x.aacc * SECONDS_PER_CLOCK
                    if x.speed > self.speedLimit(x.position) or x.speed > x.MAX_SPEED:
                        x = min(self.speedLimit(x.position), x.MAX_SPEED)
        # 计算下一帧的位置
        res = 0  # 出口等效吨数
        for x in self.carList:
            if x.uuid > 0:  # 过滤障碍
                x.position += x.speed * SECONDS_PER_CLOCK  # 微元位移，直接用末状态算就完事了
            else:
                x.capacity += 1
                if x.capacity >= JUM_PROCESS_CLOCK:  # 时间到了，事故处理完毕
                    self.carList.remove(x)  # 拿走拿走
            if x.position > self.length:  # 开完了溜了
                res += x.capacity
                self.carList.remove(x)
        return res

        # if (i.position<=x.position):    #后方车辆和自己，直接过滤
        # 	continue
        # elif(i.position>x.saftyFront()): #前方安全距离外车辆，可加速或保持最大速度直行（超车道考虑并道）
        # 	if (x.lane>0):  #超车道，观测行车道状况
        # 		for j in self.carList:
        # 			if j.lane == x.lane - 1:    #快速过滤非目标车道车辆
        #
        # 	if(x.speed==x.MAX_SPEED):
        # 		pass

# def crash(self, carList):  # 事故处理
# 	begin = carList[0]  # 记录最小里程车
# 	length = 0  # 记录事故路段长度
# 	for x in carList:
# 		length += x.length
# 		self.carList.remove(x)  # 销毁车辆
# 	jum = Car()
# 	jum.load(length=length, isCar=False)
# 	self.carList.insert(search(begin), jum)


# def search(self, Car):  # 为维护顺序表插的一个找下标函数
# 	for x in self.carList:
# 		if x.uuid==x[1].uuid:
# 			return x[0]
# 	pass


def newCar(carSize, road):
    # 随机挑一个车种
    seed = random.randint(0, (len(carSize) - 1) * 2)
    if seed > len(carSize) - 1:
        seed = 0
    # 设定车型
    if seed == 0:
        size = 0
    else:
        size = 1
    new = Car()
    new.load(
        length=carSize[seed][0],
        size=size,
        capacity=carSize[seed][1],
        MAX_SPEED=n2si(carSize[seed][2]),
        aacc=carSize[seed][4],
        dacc=carSize[seed][3],
        prior=0,
        lane=0
    )
    flag = True
    for x in road.carList:
        if new.confilct(x):
            flag = False
            break
    if flag:
        road.addCar(new)


TEST_DEEPTH = 5e3  # 测试深度
randV = 0  # 每个时钟生成车辆的概率的倒数
SPEED_LIMITS = n2si(100)  # 限速
LANE_COUNT = 2  # 车道数


def com(test_deepth=TEST_DEEPTH, randv=randV, speed_limits=SPEED_LIMITS, lane_count=LANE_COUNT):
    print("[Hanyuu debuging]")
    # 数据载入
    roadlength = open("./config/roadlength.txt")
    exp = Road(int(roadlength.read()))
    exp.speedLimits.append([0, speed_limits])
    exp.laneList.append([0, lane_count])
    print("[roadlength]" + str(exp.length))
    roadlength.close()
    # readcar = open("./config/Car.txt")
    carSize = []
    temp = []
    with open("./config/Car.txt") as car:
        for line in car:
            # temp.append(float(line.strip('\n')))
            reres = re.findall('(\d+\.?\d*)', line)
            s = []
            for x in reres:
                s.append(float(x))
            carSize.append(s)
    for x in carSize:
        print(x)
    # 往道路里塞车
    # CLOCK循环
    clock = 0
    sum = 0
    ress = 0
    while (clock <= test_deepth):
        iccc = random.randint(0, randv)
        if iccc == 0:
            newCar(carSize, exp)
        ress += exp.update()
        sum += ress
        clock += 1
        if clock % 100 == 0:
            print('[clock]' + str(clock))
            print('[sum]' + str(sum))
            print('[res]' + str(ress))
            output = open("./result/rv=" + str(randv) + ",sl=" +
                          str(speed_limits) + ",lc=" + str(lane_count) + '.log', 'a+')
            output.writelines(str(clock) + '\t' + str(sum) +
                              '\t'+str(ress) + '\n')
            output.close()
            ress = 0


if __name__ == '__main__':
    # for sl in range(5):
    #     com(speed_limits=n2si(sl * 10 + 80)
     for lc in range(5):
         com(lane_count=lc + 1)
    # for rv in range(10):
    #     com(randv=rv * 5+5)
    # for rv in range(4):
    #     com(randv=4-rv)
