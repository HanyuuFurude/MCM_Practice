# Evaluate document
## Summary

In order to evaluate the value of a school, we describe metrics in given data files. 我们主要从以下几个范围进行综合评估（1.2.3.）
====以下内容未修改……===
 Moreover, each aspect is subdivided into several secondary metrics. Take playoff performance as example, we collect postseason result (Sweet Sixteen, Final Four, etc.) per year from NCAA official website, Wikimedia and so on.    First, Analytic Hierarchy Process (AHP) Model is established to determine the weight of each metric to coaches’ evaluation grade. All metrics are adequately filled into the three-hierarchy structure, and then we obtain the metric weight based on which evaluation grade is calculated. Second, Fuzzy Synthetic Evaluation (FSE) is built to overcome weakness of excess subjective factors in AHP. This model takes data processing by membership function to generate fuzzy matrix. After that, entropy method and linear weighted method are applied to obtain evaluation grade.       To evaluate the accuracy of the two models, hit score is defined. It is supposed to reflect the difference between our results and standard rankings from several authorities such as ESPN and Sporting News. Take NCAA basketball as a case study, AHP receives 78.77 hit score while FSE gets 81.81, which indicates that FSE performs better than AHP. Afterwards, Aggregation Model (AM) can be developed by combining the two models based on hit score. The top 5 college basketball coaches, in turn, are John Wooden, Mike Krzyzewski, Adolph Rupp, Dean Smith and Bob Knight. Time line horizon does make a difference. According to turning points in NCAA history, we divide the previous century into six periods with different time weights which lead to the change of ranking. We apply our model into college women’s basketball only to find that genders do not matter. Model proves to be efficient in other sports. The ranking of college football is: Bear Bryant, Knute Rockne, Tom Osborne, Joe Paterno , Bobby Bowden, and the top 5 coaches in college hockey are Bob Johnson, Red Berenson, Jack Parker, Jerry York, Ron Mason.   We conduct sensitivity analysis on FSE to find best membership function and calculation rule. Sensitivity analysis on aggregation weight is also performed. It proves AM performs better than single model. As a creative use, top 3 presidents (U.S.) are picked out: Abraham Lincoln, George Washington, Franklin D. Roosevelt.      At last, the strength and weakness of our mode are discussed, non-technical explanation is presented and the future work is pointed as well.
***
目录
- [Evaluate document](#evaluate-document)
    - [Summary](#summary)
- [1. Introduction](#1-introduction)
    - [1.1 Background](#11-background)
    - [1.2 Previous Research](#12-previous-research)
    - [1.3 Our work](#13-our-work)
- [2. Symbols,Definitions and assumptions](#2-symbolsdefinitions-and-assumptions)
    - [2.1 Symbols and Definitions](#21-symbols-and-definitions)
    - [2.2 General Assumptions](#22-general-assumptions)
- [3. Articture our metrics](#3-articture-our-metrics)
    - [3.1 Specify evalution norms](#31-specify-evalution-norms)
    - [3.2 Collect data](#32-collect-data)
    - [3.3 Preprocess data](#33-preprocess-data)
- [4. Models](#4-models)
- [5. Target](#5-target)
    - [5.1 define](#51-define)
***
# 1. Introduction
## 1.1 Background
## 1.2 Previous Research
## 1.3 Our work
# 2. Symbols,Definitions and assumptions 
* all of the data given in data file.(expect some string fields)
* We found some most important tags.Such as //TODO...
## 2.1 Symbols and Definitions

## 2.2 General Assumptions
# 3. Articture our metrics
## 3.1 Specify evalution norms
## 3.2 Collect data
## 3.3 Preprocess data
# 4. Models
# 5. Target
## 5.1 define
> loss = 
> y = 