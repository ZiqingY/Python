# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 19:39:19 2021

@author: Altair
"""

import numpy as np

# numpy 统计函数
a=np.random.normal(0,10,(8,))
print(a)
print(np.std(a))
print(np.var(a))
print(np.average(a))
# ....


b=np.arange(15,0,-1).reshape(3,5)
print(b)
print(np.size(b))
print(np.sum(b))
print(np.mean(b,axis=1)) # 对二个维度就均值
print(np.mean(b,axis=0)) # 对第一个维度求均值
print(np.average(b,axis=0,weights=[10,2,1])) 
                         # 这里的weights代表b第一列均值权重10/12, 第二列均值权重2/12，第三列均值权重1/12；
                         # 最后对他们按照这样的权重加权平均得到结果
                         
print(np.argmax(b))      # b中所有元素的最大值扁平化后的坐标
print(np.unravel_index(np.argmax(b), b.shape)) 
                         # b中所有元素的最大值在b的坐标
print(np.ptp(b))         # 最大值最小值差
print(np.median(b))      # 中位数


'''np.random的梯度函数'''
# 一元
c=np.random.randint(0,12,(5,))
print(c)
print(np.gradient(c)) # 相当于求每一个元素处的导数

# 二元
d=np.random.randint(1,30,(5,6))
print(d)
print(np.gradient(d)) # 求出在每个元素在各个维度的偏导数

