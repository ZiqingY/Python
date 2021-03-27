# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 23:35:42 2021

@author: Altair
"""

import pandas as pd
import numpy as np

'''索引排序'''
b=pd.DataFrame(np.arange(20).reshape(4,5), index=['c','a','b','d'])
print(b)
print(b.sort_index(axis=0, ascending=True)) #默认0,True,数据行也做调整
print(b.sort_index(ascending=False))
print(b.sort_index(axis=1, ascending=False))


'''数据排序'''
# Series.sort_values(axis=0, ascending=True)
# DataFrame.sort_values(by, axis=0, ascending=True)  # by...意思是按照索引...的数据大小进行排序
# 注：NaN永远不参与排序 
c=b.sort_values(2, ascending=False) #默认索引0轴
print(c)
print(c.sort_values('a',axis=1,ascending=False)) 


'''对数据进行统计汇总'''
print(' ')
a=pd.Series(np.arange(10,14), index=['a','b','c','d'])
print(a)
print(a.describe())    # a.describe()得到的也是一个series, 可以通过索引得到想要的statistics
print(b.describe())    # b.describe()得到的就是frame了
print(b.describe()[2]) # 得到b的column2的统计汇总
print(b.describe()[2:])# 得到b统计汇总第3及行以下的所有信息

'''cummulative calculation'''
print(b.cumsum())  # 列累和
print(b.cumprod()) # 列累积
print(b.cummin())  # 列累最小
print(b.cummax())  # 列累最大


'''rolling cacluation'''
print(b)
print(b.rolling(2).sum()) # 每两行（1和2，2和3，3和4）相加
print(b.rolling(3).sum()) # 每三行（123，234）求和
# rolling(w).var()
# rolling(w).std()
# rolling(w).min()
# rolling(w).max()

'''correlation calculation'''
# a.corr(b) 得出Series a和Series b的相关系数，a和b的索引要一样
