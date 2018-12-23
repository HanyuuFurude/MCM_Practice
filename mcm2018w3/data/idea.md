# idea
## 优化目标：提升充电桩的利用率和总输出功。
$$ loss =- \{\alpha_1\cdot sigomid (\frac{\sum(\omega_i\cdot\mu_i\cdot P_i)}{\sum(\omega_i\cdot P_i)})+ \alpha_2\cdot sigomid (\frac{\sum(\omega_i\cdot\mu_i\cdot P_i)}{\alpha_3\cdot\sum(price_i)} )\}$$
> $\alpha_1$:平衡参数1(利用率权重) \
> $\omega_i$:地点权重 \
> $\mu_i$：充电桩平均利用率（该充电桩） \
> $P_i$:充电桩功率 \
> $\alpha_2$:平衡参数2（功率权重）\
> $\alpha_3$:平衡参数3（表现优化权重）\
> $price_i$:充电桩投入（成本）

> * 为何使用sigomid：提升综合指标的评定能力，方式出现单一指标得分高零一指标得分低的情况。
> * $alpha_1$$alpha_2$如何计算：利用加油站的利用率和日消耗量匹配
> * $alpha_3$:用于调整sogomid函数的区分能力，设定为一般电桩的sigomid输出为0左右即可，所有的指标进行比较时需保证$\alpha_3$一致，否则没有指导意义。
> * 如何计算$\omega_i$:$\omega_i$依附与城市节点，其相对比值和不同城市的汽车持有数或人数或经济能力与加油站的总供给量成之比相等（查询数据）。平均值为1.
> * 如何计算$\mu_i$:初始值，充电桩平均利用率（查询数据），后期在模拟过程中根据历史使用情况动态更改（历史加权）
> * $P_i$:产品规格
> * $price_i$:产品规格
## task 01
