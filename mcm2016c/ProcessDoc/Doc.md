# An Optimal Strategy of Donation for Educational Purpose


# Summary

为了确定最佳捐赠策略，本文提出了一个基于适用于慈善组织的投资回报率（ROI）原始定义的数据动机模型。

In order to evaluate the value of a school, we describe metrics in given data files. We selected two main species vector.First, 
我们使用了插补法对数据进行了补全和清洗，通过先断知识，我们为其赋予了初始分值并通过后期处理给出了相应的权重。

其次，为了解决由高维数据引起的问题，我们采用主成分分析法（PCA）将数据降维，得到新的特征向量，即新的绩效指标。 

接下来，我们开发了一个综合指数，称为绩效指数，以量化学生的教育表现。 绩效指数是由上一步PCA分析出的绩效指标的线性组合，其系数则是通过循环神经网络（CNN）一步步拟合得出。 

最后，我们计算ROI，定义为性能指数的增加而不是捐赠量的增加。 此投资回报率是机构特定的，取决于捐赠金额的增加。 通过采用两步ROI最大化算法，我们确定最优投资策略。



***
目录
- [An Optimal Strategy of Donation for Educational Purpose](#an-optimal-strategy-of-donation-for-educational-purpose)
- [Summary](#summary)
- [给CEO的信](#%E7%BB%99ceo%E7%9A%84%E4%BF%A1)
- [下面是建议的投资策略](#%E4%B8%8B%E9%9D%A2%E6%98%AF%E5%BB%BA%E8%AE%AE%E7%9A%84%E6%8A%95%E8%B5%84%E7%AD%96%E7%95%A5)
- [1. Introduction](#1-introduction)
    - [1.1 Statement of the Problem](#11-statement-of-the-problem)
    - [1.2 Detailed Definitions & Assumptions](#12-detailed-definitions--assumptions)
        - [1.2.1 Detailed Definitions](#121-detailed-definitions)
        - [1.2.2 Assumption](#122-assumption)
    - [1.3 The Advantages of Our Model](#13-the-advantages-of-our-model)
- [2. Symbols,Definitions and assumptions](#2-symbolsdefinitions-and-assumptions)
    - [2.1 Symbols and Definitions](#21-symbols-and-definitions)
    - [2.2 General Assumptions](#22-general-assumptions)
- [3. Articture our metrics](#3-articture-our-metrics)
    - [3.1 数据维度过高的问题](#31-%E6%95%B0%E6%8D%AE%E7%BB%B4%E5%BA%A6%E8%BF%87%E9%AB%98%E7%9A%84%E9%97%AE%E9%A2%98)
    - [3.2 利用主成分分析法（PCA）降低数据维度](#32-%E5%88%A9%E7%94%A8%E4%B8%BB%E6%88%90%E5%88%86%E5%88%86%E6%9E%90%E6%B3%95pca%E9%99%8D%E4%BD%8E%E6%95%B0%E6%8D%AE%E7%BB%B4%E5%BA%A6)
- [4. Determining the Performance Index](#4-determining-the-performance-index)
- [5. Determining Investment Strategy based on ROI](#5-determining-investment-strategy-based-on-roi)
- [6. 计算流程](#6-%E8%AE%A1%E7%AE%97%E6%B5%81%E7%A8%8B)
    - [6.1 数据清洗与处理](#61-%E6%95%B0%E6%8D%AE%E6%B8%85%E6%B4%97%E4%B8%8E%E5%A4%84%E7%90%86)
- [7. Conclusions and Discussion](#7-conclusions-and-discussion)
    - [7.1 Conclusions](#71-conclusions)
    - [7.2 Limitation and extensions](#72-limitation-and-extensions)
***
# 给CEO的信
>
>亲爱的Chiang，
>
>我们的团队提出了一个绩效指标，用于量化学生的每个机构的教育表现，并为Goodgrant Foundation等慈善组织适当定义投资回报率（ROI）。建立数学模型是为了在确定捐赠对绩效产生影响的机制后帮助预测投资回报。
>
>最优投资策略是通过最大化估计的投资回报来确定的。更具体地说，综合绩效指数是在考虑了所有可能的绩效指标（如毕业率和毕业生收入）之后制定的。绩效指数的构建是为了代表学校的表现以及学院为学生和社区带来的积极影响。从这个角度来看，我们的定义设法捕捉捐赠的社会效益。然后我们采用主成分分析方法来找出性能贡献变量，这些变量强烈影响性能指标。我们拟合了这些变量和捐赠金额之间的关系，以预测每个绩效贡献变量的价值相对于捐赠金额的变化。我们通过将每个绩效贡献变量的值与捐赠金额和每个绩效贡献变量对绩效指数的影响相乘，然后将所有绩效的产品相加，计算ROI（定义为绩效指标相对于捐赠金额的增加）贡献变量。根据选择算法最大化投资回报后，决定最优投资策略。
>
>总之，我们的模型成功地制定了一项投资策略，包括目标机构清单和每个机构的投资金额。 （第1年的清单附在信件的末尾）。投资的持续时间也可以根据我们的模型确定。由于模型和评估方法完全是数据驱动的，没有包含任意标准，因此它适用于解决未来的慈善教育投资问题。我们坚信，我们的模式可以有效提高慈善教育投资的效率，并为最佳地提高学生的教育绩效提供一种适当和可行的方法。
# 下面是建议的投资策略
| NO | INSTNM                                               | UNITID | SCORE       | INVESTMENT      |
|----|------------------------------------------------------|:-------|------------:|----------------:|
| 1  | Medical College of Wisconsin                         | 239169 | 0.999459574 | $5,086,407.39   |
| 2  | Albany Medical College                               | 188580 | 0.997669333 | $5,077,296.57   |
| 3  | A T Still University of Health Sciences              | 177834 | 0.997564058 | $5,076,760.81   |
| 4  | West Virginia School of Osteopathic Medicine         | 237880 | 0.997476675 | $5,076,316.10   |
| 5  | University of Massachusetts Medical School Worcester | 166708 | 0.996238404 | $5,070,014.35   |
| 6  | New York Medical College                             | 193830 | 0.99406238  | $5,058,940.22   |
| 7  | Rosalind Franklin University of Medicine and Science | 145558 | 0.993442022 | $5,055,783.12   |
| 8  | Philadelphia College of Osteopathic Medicine         | 215123 | 0.988850119 | $5,032,414.20   |
| 9  | University of North Texas Health Science Center      | 228909 | 0.982072607 | $4,997,922.37   |
| 10 | Baylor College of Medicine                           | 223223 | 0.980199221 | $4,988,388.42   |
| 11 | Meharry Medical College                              | 220792 | 0.978832453 | $4,981,432.71   |
| 12 | Western University of Health Sciences                | 112525 | 0.976554211 | $4,969,838.38   |
| 13 | SUNY Downstate Medical Center                        | 196255 | 0.975377605 | $4,963,850.45   |
| 14 | University of California-San Francisco               | 110699 | 0.973446364 | $4,954,022.06   |
| 15 | Midwestern University-Downers Grove                  | 143853 | 0.971981321 | $4,946,566.23   |
| 16 | Midwestern University-Glendale                       | 423643 | 0.971949743 | $4,946,405.52   |
| 17 | MCPHS University                                     | 166656 | 0.971513982 | $4,944,187.87   |
| 18 | Upstate Medical University                           | 196307 | 0.968459056 | $4,928,640.87   |
| 19 | St Louis College of Pharmacy                         | 179265 | 0.967265721 | $4,922,567.79   |
| 20 | Samuel Merritt University                            | 122296 | 0.967202212 | $4,922,244.59   |
|    |                                                      |        |             | $100,000,000.00 |

***
# 1. Introduction

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
* The evaluation model is based entirely on data and there are few subjective or arbitrary decision rules.
* Our model successfully identifies potential mechanisms, not just indicators such as graduation rates.
* Our model makes full use of cross-section data and does not require time series data to produce reasonable results
A
# 2. Symbols,Definitions and assumptions 
* all of the data given in data file.(expect some string fields)
* We found some most important tags.Such as //TODO...
## 2.1 Symbols and Definitions

## 2.2 General Assumptions
#  3. Articture our metrics
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

# 6. 计算流程
## 6.1 数据清洗与处理
>  因为慈善机构给出的学校比数据集中统计的学校数量要少很多，因此首要步骤是将这些备选学校的数据筛选出来，并且将学校官网、研究生数量等无关因素排除，最终筛选出毕业率、毕业后还款率、得奖的学生人数等p个与回报指数相关的指标。
 *  问题：我们发现数据文件中存在大量缺失值，数据集中含有缺失项的变量成为不完全变量，从缺失的分布我们认为属于随机缺失(missing random,MAR)。对于随机缺失，删除是、记录时不合适的，随机缺失可以通过已知变量对缺失值进行估计。如果单纯舍去缺失项会导致模型失准和信息丢失。
* 必要性:数据缺失在许多研究领域都是一个复杂的问题。对数据挖掘来说，缺省值的存在，造成了以下影响： 
	* 系统丢失了大量的有用信息；
	* 系统中所表现出的不确定性更加显著，系统中蕴涵的确定性成分更难把握；
	* 包含空值的数据会使挖掘过程陷入混乱，导致不可靠的输出。
* 该流程致力于避免数据过分拟合所建的模型，这一特性使得它难以通过自身的算法去很好地处理不完整数据。因此，缺省值需要通过专门的方法进行推导、填充等，以减少数据挖掘算法与实际应用之间的差距。
* 处理方法：处理不完整数据集的方法主要有三大类：删除元组、数据补齐、不处理。
	* 删除元组：也就是将存在遗漏信息属性值的对象（元组，记录）删除，从而得到一个完备的信息表。这种方法简单易行，在对象有多个属性缺失值、被删除的含缺失值的对象与初始数据集的数据量相比非常小的情况下非常有效，类标号缺失时通常使用该方法。 
然而，这种方法却有很大的局限性。它以减少历史数据来换取信息的完备，会丢弃大量隐藏在这些对象中的信息。在初始数据集包含的对象很少的情况下，删除少量对象足以严重影响信息的客观性和结果的正确性；因此，当缺失数据所占比例较大，特别当遗漏数据非随机分布时，这种方法可能导致数据发生偏离，从而引出错误的结论。
说明:删除元组，或者直接删除该列特征，有时候会导致性能下降。
	* 数据补齐：这类方法是用一定的值去填充空值，从而使信息表完备化。通常基于统计学原理，根据初始数据集中其余对象取值的分布情况来对一个缺失值进行填充。数据挖掘中常用的有以下几种补齐方法：
        * filling manually
        由于最了解数据的还是用户自己，因此这个方法产生数据偏离最小，可能是填充效果最好的一种。然而一般来说，该方法很费时，当数据规模很大、空值很多的时候，该方法是不可行的。
        * Treating Missing Attribute values as Special values
        将空值作为一种特殊的属性值来处理，它不同于其他的任何属性值。如所有的空值都用unknown填充。这样将形成另一个有趣的概念，可能导致严重的数据偏离，一般不推荐使用。
        * Mean/Mode Completer
        将初始数据集中的属性分为数值属性和非数值属性来分别进行处理。 如果空值是数值型的，就根据该属性在其他所有对象的取值的平均值来填充该缺失的属性值； 如果空值是非数值型的，就根据统计学中的众数原理，用该属性在其他所有对象的取值次数最多的值(即出现频率最高的值)来补齐该缺失的属性值。与其相似的另一种方法叫条件平均值填充法（Conditional Mean Completer）。在该方法中，用于求平均的值并不是从数据集的所有对象中取，而是从与该对象具有相同决策属性值的对象中取得。 这两种数据的补齐方法，其基本的出发点都是一样的，以最大概率可能的取值来补充缺失的属性值，只是在具体方法上有一点不同。与其他方法相比，它是用现存数据的多数信息来推测缺失值。
        * Hot deck imputation
        对于一个包含空值的对象，热卡填充法在完整数据中找到一个与它最相似的对象，然后用这个相似对象的值来进行填充。不同的问题可能会选用不同的标准来对相似进行判定。该方法概念上很简单，且利用了数据间的关系来进行空值估计。这个方法的缺点在于难以定义相似标准，主观因素较多。
        * K-means clustering
        先根据欧式距离或相关分析来确定距离具有缺失数据样本最近的K个样本，将这K个值加权平均来估计该样本的缺失数据。
        * 使用所有可能的值填充（Assigning All Possible values of the Attribute）
        用空缺属性值的所有可能的属性取值来填充，能够得到较好的补齐效果。但是，当数据量很大或者遗漏的属性值较多时，其计算的代价很大，可能的测试方案很多。
        * Combinatorial Completer
        用空缺属性值的所有可能的属性取值来试，并从最终属性的约简结果中选择最好的一个作为填补的属性值。这是以约简为目的的数据补齐方法，能够得到好的约简结果；但是，当数据量很大或者遗漏的属性值较多时，其计算的代价很大。
        * Regression
        基于完整的数据集，建立回归方程。对于包含空值的对象，将已知属性值代入方程来估计未知属性值，以此估计值来进行填充。当变量不是线性相关时会导致有偏差的估计。
        * 期望值最大化方法（Expectation maximization，EM）
        EM算法是一种在不完全数据情况下计算极大似然估计或者后验分布的迭代算法。在每一迭代循环过程中交替执行两个步骤：E步（Excepctaion step,期望步），在给定完全数据和前一次迭代所得到的参数估计的情况下计算完全数据对应的对数似然函数的条件期望；M步（Maximzation step，极大化步），用极大化对数似然函数以确定参数的值，并用于下步的迭代。算法在E步和M步之间不断迭代直至收敛，即两次迭代之间的参数变化小于一个预先给定的阈值时结束。该方法可能会陷入局部极值，收敛速度也不是很快，并且计算很复杂。
        * Multiple Imputation，MI
        多重填补方法分为三个步骤： 为每个空值产生一套可能的填补值，这些值反映了无响应模型的不确定性；每个值都被用来填补数据集中的缺失值，产生若干个完整数据集合。每个填补数据集合都用针对完整数据集的统计方法进行统计分析。对来自各个填补数据集的结果进行综合，产生最终的统计推断，这一推断考虑到了由于数据填补而产生的不确定性。该方法将空缺值视为随机样本，这样计算出来的统计推断可能受到空缺值的不确定性的影响。该方法的计算也很复杂。
        * C4.5
        通过寻找属性间的关系来对遗失值填充。它寻找之间具有最大相关性的两个属性，其中没有遗失值的一个称为代理属性，另一个称为原始属性，用代理属性决定原始属性中的遗失值。这种基于规则归纳的方法只能处理基数较小的名词型属性。
    * 就几种基于统计的方法而言，删除元组法和平均值法差于热卡填充法、期望值最大化方法和多重填充法；回归是比较好的一种方法，但仍比不上hot deck和EM；EM缺少MI包含的不确定成分。值得注意的是，这些方法直接处理的是模型参数的估计而不是空缺值预测本身。它们合适于处理无监督学习的问题，而对有监督学习来说，情况就不尽相同了。譬如，你可以删除包含空值的对象用完整的数据集来进行训练，但预测时你却不能忽略包含空值的对象。另外，C4.5和使用所有可能的值填充方法也有较好的补齐效果，人工填写和特殊值填充则是一般不推荐使用的。
    * 选取：
        * 由于数据缺失项较多，删除元组会造成大量有效数据失效，不处理会导致计算效果可信度低下，我们选择了补齐元素；
        * 由于数据缺失项较多，
            * filling manually不现实，舍去。 
            * Treating Missing Attribute values as Special values会导致严重的数据偏离，故不采用。
 * 计算：为了处理大量数据，我们使用了tensorflow作为计算工具，依照算法模型搭建了shallow网络以计算Widget。为了将输出值控制在限定范围内的同时保证合理分布，我们使用对数几率回归模型对输出进行约束。
 *  数据标准化处理
    已知有p个指标，为了解决量纲不同所带来的影响，我们需要对原始数据进行标准化处理，将$x_i$转化成标准值$\hat{x_i}$：
    $$
    \hat{x_{ij}}=\frac{x_{ij}-\mu_{j}}{s_j},i=1,2,3,...,n,j=1,2,3,...,p\tag{2.1}\\
    \mu_j=\frac{1}{n}\sum_{i=1}^{n}{x_{ij}}\\
    s_j=\sqrt{\frac{1}{n-1}\sum_{j=1}^{n}{(x_{ij}-\mu_j)}^2},j=1,2,...,p
    $$
    $\mu_j,s_j$是第i个指标的样本均值和样本标准差。



# 7. Conclusions and Discussion

## 7.1 Conclusions

This paper manages to develop a fully data-based model to produce a provi- dent investment strategy that maximizing ROI. Our model exhibits a great potential in drawing the conclusions below:

* We formulate a performance index for each institution with principal component analysis and develop an appropriate concept for return of investment (ROI) for the charitable foundations like Goodgrant Foundation. 

* We derive the relation between the performance contributing variables and donation amount from a GAM fitting model to predict ROI of performance contributing variables. 

* The final list of selected institutions and appropriate amount of donation is determined by a two-step selection algorithm.

## 7.2 Limitation and extensions

 Though our model successfully produced an investment strategy, it can be improved in several ways:

* Since only cross-section data is available, our results of time duration of donation can be improved if we have access to time-series. 

* Our model only allows for a relatively simple linear model. A more gen- eral selection method is needed when applying to a complicated model.


