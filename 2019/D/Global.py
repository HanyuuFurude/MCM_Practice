import reader_MRCD
SECOND_PER_FRAME=0 #每帧秒数
clockCount=0 #$:时钟计数
savedPopulation=0 #$:出逃人数
score=0 #$:评估分

### 灾害

# *   $dCase$:灾害类型
# *   $dPosition$:灾害原生发生位置
# *   $dTrend$:灾害流动趋势

class disaster:
    def __init__(self,type,local,trend):
        self.dCase=type
        self.dPos=local
        self.dTrend=trend

    def trend:
        reader_MRCD.capacity[self.self.dPos]=0


