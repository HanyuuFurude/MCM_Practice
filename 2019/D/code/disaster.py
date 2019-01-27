# 灾害

# *   $dCase$:灾害类型
# *   $dPosition$:灾害原生发生位置
# *   $dTrend$:灾害流动趋势


class disaster:
    def __init__(self, case, local, trend):
        self.case = case
        self.position = local
        self.trend = None

    def flow(self): #险情流动
        if self.case == 1:  #蔓延型
            pass
        elif self.case == 0:  #转移型
            pass