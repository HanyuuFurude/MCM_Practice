problem C论文（中文版）

# An Optimal Strategy of Donation for Educational Purpose


# 摘要

为了确定最佳捐赠策略，本文提出了一个基于适用于慈善组织的投资回报率（ROI）原始定义的数据动机模型。

首先，我们对数据进行处理和清洗。在这个过程中，我们提取出需要的数据，并利用聚类后的均值填补缺失的数据。

其次，为了解决由高维数据引起的问题，我们采用主成分分析法（PCA）将数据降维，得到新的特征向量，即新的绩效指标。 

接下来，我们开发了一个综合指数，称为绩效指数，以量化学生的教育表现。 绩效指数是由上一步PCA分析出的绩效指标的线性组合，其系数则是通过循环神经网络（CNN）一步步拟合得出。 

最后，我们计算ROI，定义为性能指数的增加而不是捐赠量的增加。 此投资回报率是机构特定的，取决于捐赠金额的增加。 通过采用两步ROI最大化算法，我们确定最优投资策略。







>​								给CEO的信
>
>亲爱的Chiang，
>
>我们的团队提出了一个绩效指标，用于量化学生的每个机构的教育表现，并为Goodgrant Foundation等慈善组织适当定义投资回报率（ROI）。建立数学模型是为了在确定捐赠对绩效产生影响的机制后帮助预测投资回报。
>
>最优投资策略是通过最大化估计的投资回报来确定的。更具体地说，综合绩效指数是在考虑了所有可能的绩效指标（如毕业率和毕业生收入）之后制定的。绩效指数的构建是为了代表学校的表现以及学院为学生和社区带来的积极影响。从这个角度来看，我们的定义设法捕捉捐赠的社会效益。然后我们采用主成分分析方法来找出性能贡献变量，这些变量强烈影响性能指标。我们拟合了这些变量和捐赠金额之间的关系，以预测每个绩效贡献变量的价值相对于捐赠金额的变化。我们通过将每个绩效贡献变量的值与捐赠金额和每个绩效贡献变量对绩效指数的影响相乘，然后将所有绩效的产品相加，计算ROI（定义为绩效指标相对于捐赠金额的增加）贡献变量。根据选择算法最大化投资回报后，决定最优投资策略。
>
>总之，我们的模型成功地制定了一项投资策略，包括目标机构清单和每个机构的投资金额。 （第1年的清单附在信件的末尾）。投资的持续时间也可以根据我们的模型确定。由于模型和评估方法完全是数据驱动的，没有包含任意标准，因此它适用于解决未来的慈善教育投资问题。我们坚信，我们的模式可以有效提高慈善教育投资的效率，并为最佳地提高学生的教育绩效提供一种适当和可行的方法。


# TODO.. 这里请补充最后的投资学校名单！！！！！！！！！！

# 1 Introduction

## 1.1 Statement of the Problem

There exists no doubt in the significance of postsecondary education to the development of society, especially with the ascending need for skilled employees capable of complex work. Nevertheless, U.S. ranks only 11th in the higher education attachment worldwide, which makes the financial support from large charitable organizations necessary.

As it’s essential for charitable organizations to maximize the effectiveness of donations, an objective and systematic assessment model is in demand to develop appropriate investment strategies. To achieve this goal, several large foundations like Gates Foundation and Lumina Foundation have developed different evaluation approaches, where they mainly focus on spe- cific indexes like attendance and graduation rate. In other empirical literature, a Forbes ap- proach (Shifrin and Chen,2015) proposes a new indicator called the Grateful Graduates Index, using the median amount of private donations per student over a 10-year period to measure the return on investment. Also, performance funding indicators (Burke,2002, Cave,1997, Ser- ban and Burke,1998,Banta et al,1996), which include but are not limited to external indicators like graduates’ employment rate and internal indicators like teaching quality, are one of the
most prevailing methods to evaluate effectiveness of educational donations.

However, those methods also arise with widely acknowledged concerns (Burke,1998). Most of them require subjective choice of indexes and are rather arbitrary than data-based. And they perform badly in a data environment where there is miscellaneous cross-section data but scarce time-series data. Besides, they lack quantified analysis in precisely predicting or measuring the social benefits and the positive effect that the investment can generate, which serves as one of the targets for the Goodgrant Foundation.

In accordance with Goodgrant Foundation’s request, this paper provides a prudent definition of return on investment (ROI) for charitable organizations, and develops an original data-motivated model, which is feasible even faced with tangled cross-section data and absent time-series data, to determine the optimal strategy for funding. The strategy contains selection of institutions and distribution of investment across institutions, time and regions.

## 1.2 Detailed Definitions & Assumptions

### 1.2.1 Detailed Definitions

|     name     |                        definition                         |      denotation       |
| :----------: | :-------------------------------------------------------: | :-------------------: |
|   学校属性   |         评价一所学校的回报的数据值，共有p个数据值         |  $x_1,x_2,x_3...x_p$  |
|  school_num  |                number of candidate schools                |           n           |
|   绩效指数   |                    对一所学校的总评价                     |           Y           |
| 简化后的指标 | 经过主成分分析后得到的一所学校的主要数据，共共有j个数据值 | $Z_1，Z_2，Z_3...Z_j$ |
|   捐赠金额   |          对一所学校的捐赠金额，在一个假设集合中           |         $Z_i$         |
|              |                                                           |                       |

### 1.2.2 Assumption

1. Stability. We assume data of any institution should be stable without the impact from outside. To be specific, the key factors like the donation amount and the performance index should remain unchanged if the college does not receive new donations. 
2. Goodgrant Foundation’s donation (Increase in donation amount) is discrete rather than continuous. This is reasonable because each donation is usually an integer multiple of a minimum amount, like $1m. After referring to the data of other foundations like Lumina Foundation, we recommend donation amount should be one value in the set below:
{500000, 1000000, 1500000, ..., 10000000}
3. The performance index is a linear composition of all given performance indicators.
4. Performance contributing variables linearly affect the performance index. 
5. Increase in donation amount affects the performance index through performance contributing
variables. 
6. The impact of increase in donation amount on performance contributing variables contains 2 parts: homogenous one and heterogenous one. The homogenous influence is repre- sented by a smooth function from donation amount to performance contributing variables. And the heterogenous one is represented by deviation from the function.

## 1.3 The Advantages of Our Model

Our model has many advantages in the application:
• The evaluation model is based entirely on data and there are few subjective or arbitrary decision rules.
• Our model successfully identifies potential mechanisms, not just indicators such as graduation rates.
• Our model makes full use of cross-section data and does not require time series data to produce reasonable results



# 2. Data preprocessing

## 2.1 数据清洗

因为慈善机构给出的学校比数据集中统计的学校数量要少很多，因此首要步骤是将这些备选学校的数据筛选出来，并且将学校官网、研究生数量等无关因素排除，最终筛选出毕业率、毕业后还款率、得奖的学生人数等p个与回报指数相关的指标。

## 2.2 填补缺失数据

因为数据集中较多重要属性，如还款率、毕业率等都存在NULL，因此需要选择一种合理的方式将缺失数据预测出来。首先考虑利用平均值对数据进行填补，但是这样的方式会带来很大的误差。为了数据精度，最终采用了k-means聚类后取均值的方法对数据进行填补。

## 2.3 数据标准化处理

已知有p个指标，为了解决量纲不同所带来的影响，我们需要对原始数据进行标准化处理，将$x_i$转化成标准值$\hat{x_i}$：
$$
\hat{x_{ij}}=\frac{x_{ij}-\mu_{j}}{s_j},i=1,2,3,...,n,j=1,2,3,...,p\tag{2.1}\\
\mu_j=\frac{1}{n}\sum_{i=1}^{n}{x_{ij}}\\
s_j=\sqrt{\frac{1}{n-1}\sum_{j=1}^{n}{(x_{ij}-\mu_j)}^2},j=1,2,...,p
$$
$\mu_j,s_j$是第i个指标的样本均值和样本标准差。


# 3 Reduce the data dimension

## 3.1 数据维度过高的问题

因为考虑的相关因素太多，导致结果过多，变量间的相关度高，为建模带来不便。因此希望能够用较少的变量来解释资料中大部分变异，将相关性高的变量转化成彼此相互独立或不相关的变量。所以，我们最终选择主成分分析法。

## 3.2 利用主成分分析法（PCA）降低数据维度

$x_1,x_2,...,x_p$为p个描述学校的原始特征，$c_1,c_2,...,c_p$表示各个变量的权重。为每个特征值加一个权重并求和得到s：
$$
s=c_1x_1+c_2x_2+...+c_px_p
$$
我们希望选择适当的权重能够更好地表现学校的效益，每个学校对应一个综合成绩，记为$s_1,s_2,...,s_n$,n为学校数量。如果这些数值很分散，就表明它区分的很好，即寻找这样一系列参数c，使得$s_1,s_2,s_3,...,s_n$尽可能的分散。它的统计学定义描述如下：

设$X_1,X_2,...,X_p$表示以$x_1,x_2,...,x_p$为样本观测值的随机变量，如果能找到$c_1,c_2,...,c_p$使得
$$
Var(c_1X_1+c_2X_2+...+c_pX_p)\tag{3.1}
$$
的值达到最大，由于方差反映了数据差异的程度，也就表明我们抓住了这p个变量的最大变异。同该表达式必须加上一个限制，否则权值可能选择无穷大而没有意义，这里我们规定
$$
c_1^2+c_2^2+...+c_p^2=1             \tag{3.2}
$$
至此我们得到一个主成分方向$\vec{a}=[c_1,c_2,...,c_p]$,它是一个p-维空间的单位向量。但是一个主成分不足以代表原来的p个变量，因此需要寻找多个主成分，且第二个主成分不应该再包含第一个主成分的信息，即让这两个主成分的协方差为0，方向正交。

设$Z_i$表示第i个主成分，$i=1,2,...,p,可设
$$
\begin{equation} 
\left\{ 
\begin{array}{lr} 
Z_1=c_{11}X_1+c_{12}X_2+...+c_{1p}X_p,\\ 
Z_2=c_{21}X_1+c_{22}X_2+...+c_{2p}X_p, \\ 
...\\
Z_{p}=c_{p1}X_1+c_{p2}X_2+...+c_{pp}X_p, 
\end{array} \right. \end{equation}\tag{3.3}
$$
对于每个i，均满足等式（3.2）。接着需要确定$j(j<p)$的数值，即降低维度后的指标个数。

计算每一个主成分方向对应的的特征值$\lambda_j(j=1,2,...,p)$的信息贡献率和累积贡献率。称
$$
b_j=\frac{\lambda_j}{\sum_{k=1}^{p}\lambda_k}\tag{3.4}
$$
为主成分$y_i$的信息贡献率。
$$
\alpha_j=\frac{\sum_{k=1}^{j}{\lambda_k}}{\sum_{k=1}^{p}{\lambda_k}}\tag{3.5}
$$
为主成分$y_1,y_2,...,y_j$的累积贡献率。当$\alpha_j$接近于1时，选择前j个指标变量，代替原来的p个指标。

# 4. Determining the Performance Index

由上面的主成分分析法可以得到j个主要的变量，但是他们都是标准化之后的值，并不具备原来的精确意义。至此，构件评价指数的准备工作就已完成，计算综合得分
$$
Z=\sum_{j=1}^{p}{b_jy_j}
$$


# 5. Determining Investment Strategy based on ROI

Since we have already approximated the linear relation between the performance index with the 3 performance contributing variables, we want to know how increase in donation changes them. In this paper, we use Generalized Adaptive Model (GAM) to smoothly fit the relations. Generalized Adaptive Model is a generalized linear model in which the dependent variable depends linearly on unknown smooth functions of independent variables. The fitted curve of percentage of students who receive a Pell Grant is depicted below in Fig 4 (see the other two fitted curves in Appendix):

![1543398609995](C:\Users\zmj\AppData\Roaming\Typora\typora-user-images\1543398609995.png)

A Pell Grant is money the U.S. federal government provides directly for students who need it to pay for college. Intuitively, if the amount of donation an institution receives from other sources such as private donation increases, the institution is likely to use these donations to alleviate students’ financial stress, resulting in percentage of students who receive a Pell Grant. Thus it is reasonable to see a fitted curve downward sloping at most part. Also, in common sense, an increase in donation amount would lead to increase in the performance index. 

![1543398671892](C:\Users\zmj\AppData\Roaming\Typora\typora-user-images\1543398671892.png)

Again, we use fitted curve of percentage of students who receive a Pell Grant as an example. We modeled the blue fitted curve to represent the homogeneous relation between percentage of students who receive a Pell Grant and donation amount. Recall fitted ROI of percentage of students who receive a Pell Grant (f ROI1) is change in fitted values (∆f) over increase in donation amount (∆X). So fROI1 = ∆f/∆X According to assumption A2, the amount of each Goodgrant Foundation’s donation falls into apre-specifiedset,namely {500000,1000000,1500000,...,10000000}.

Sowegetasetofpossible fitted ROI of percentage of students who receive a Pell Grant (fROI1). Clearly, fROI1 is de- pendent on both donation amount (X) and increase in donation amount (∆X). Calculation of fitted ROIs of other performance contributing variables is similar.
$$
ROI=\frac{Z}{F}
$$
The next step is to develop an optimal strategy including a list of institutions to be sponsored and the appropriate amount of money given to each institution. We adopt a two-step selection algorithm to find the global optimal allocation strategy. Since we have a finite set of possible ROI for every institution. The first step is to compare ROI among each institution’s set. By maximizing ROI for each institution, we determine the optimal amount of investment on each institution if we invest. Then, the next step is to rank all institutions with their respective maximal ROI. Given the budget constraint of money available ($100m), we pick up the institutions with the largest potential to improve on the performance indicator, namely the largest maximal ROI, until we exhaust the budget.

# 6. Conclusions and Discussion

## 6.1 Conclusions

This paper manages to develop a fully data-based model to produce a provi- dent investment strategy that maximizing ROI. Our model exhibits a great potential in drawing the conclusions below:

* We formulate a performance index for each institution with principal component analysis and develop an appropriate concept for return of investment (ROI) for the charitable foundations like Goodgrant Foundation. 

* We derive the relation between the performance contributing variables and donation amount from a GAM fitting model to predict ROI of performance contributing variables. 

* The final list of selected institutions and appropriate amount of donation is determined by a two-step selection algorithm.

## 6.2 Limitation and extensions

 Though our model successfully produced an investment strategy, it can be improved in several ways:

* Since only cross-section data is available, our results of time duration of donation can be improved if we have access to time-series. 

* Our model only allows for a relatively simple linear model. A more gen- eral selection method is needed when applying to a complicated model.









