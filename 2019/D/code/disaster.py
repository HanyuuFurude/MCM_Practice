# 灾害

# *   $dCase$:灾害类型
# *   $dPosition$:灾害原生发生位置
# *   $dTrend$:灾害流动趋势


class disaster:
    def __init__(self, case, local, trend):
        self.dCase = case
        self.dPos = local
        self.dTrend = trend

    def trend(self):
        pass
