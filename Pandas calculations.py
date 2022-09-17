# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 22:51:59 2021

@author: Altair
"""

import pandas as pd
import numpy as np

a=pd.DataFrame(np.arange(12).reshape(3,4))
b=pd.DataFrame(np.arange(20).reshape(4,5))
print(a)
print(b)
print(' ')



'''依旧无法对不吻合的位置进行运算'''
print(a+b)
print(a*b)



'''填充不吻合部分运算结果: add sub mul div'''
# 例子：
print(b.add(a,fill_value=100)) #给a填充了100以后再加b
print(b.mul(a,fill_value=0))   #给a填充了0以后再乘以b
print(a.mul(b,fill_value=0))   #和上一行结果一样，说明填充一定是填充少的



'''DataFrame和Series的运算'''
c=pd.Series([1,2,3,4])
print(c)
print(b-c)                     # b每一列减c
print(b.sub(c,axis=0))         # b第一列减c



'''逻辑运算'''
d=pd.DataFrame(np.arange(12,0,-1).reshape(3,4))
print(' ')
print(d)
print(a>d) # frame和frame比较，必须要size一致
print(a>c) # frame和series比较，每一列与c进行比较
print(c>0)
