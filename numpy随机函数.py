# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 18:47:45 2021

@author: Altair
"""

import numpy as np

'''np.random函数'''
a=np.random.rand(2,3,4) # 0到1均匀分布+维度2×3×4
b=np.random.randn(2,3,4) # 标准正态分布+维度2×3×4
c=np.random.randint(1,100,(3,4))
print(a)
print(b)
print(c)


'''seed #这里把seed相关代码失效，免得下面生成的随机量都被铆钉
print(' ')
np.random.seed(10)               # 用seed(10)标记特定的随机生成数组
s=np.random.randint(1,100,(3,4)) 
print(s)
np.random.seed(10)               # 引用标记
s1=np.random.randint(1,100,(3,4))
print(s1)                        # 发现在seed10下运行得到随机结果一样
'''



'''对给定ndarray第一维随机排序：shuffle(a)  permutation(a)'''
d=np.random.randint(1,100,(5,2))
print(d)
np.random.shuffle(d)
print(d) # 改变d本身

e=np.random.randint(1,100,(4,5))
print(e)
e1=np.random.permutation(e)
print(e1)
print(e) # 不改变e本身


'''从一位数组中抽取，组成矩阵'''  
x=np.random.randint(1,200,(15,)) #从1到200中随机抽取15个数组成一维数组
print(x)
print(np.random.choice(x,(2,3),replace=True,p=x/np.sum(x)))
# 从x中抽取元素组成2×3数组，允许重复，抽到各个数的概率为其大小占sum(x)的比重


'''特定分布'''
print(np.random.uniform(0,10,(2,3)))
print(np.random.normal(0,1,(1,6)))
print(np.random.poisson(0.5,(4,4))) 
     #0.5为事件发生概率，(4,4)生成的4×4的服从泊松分布变量组成的数组的维度