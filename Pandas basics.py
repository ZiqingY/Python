# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:39:07 2021

@author: Altair
"""

import pandas as pd
import numpy as np

'''pandas有两种数据类型：series和dataframe
先介绍Series'''
a=pd.Series([9,8,7,6])
print(a)  # 左边是索引

b = pd.Series([9,8,7,6], index=['a','b','c','d'])
print(b)  # 命名索引

b1=pd.Series(250, index=['a','b','c','d'])
print(b1) # 数据值为单一值

c=pd.Series({'a':9,'b':8,'c':7})
print(c)  # 另一种定义series方法

d=pd.Series({'a':9,'b':8,'c':7}, index=['a','b','c','d'])
print(d)  # 上一种方法 + 强行定义index，允许缺失index对应的数据值

e = pd.Series(np.arange(6), index=['a','b','c','d','e','f'])
print(e)  # 用0开始6个整数填充a到f的index

e1 = pd.Series(np.arange(5), index=np.arange(9,4,-1))
print(e1) #用0到开始5个整数填充9到4倒序的index



'''对series的操作'''
print('.........................................')
print(e)
print(e.index)
print(e.values)
print(e[['a','b']])  #自定义索引a和b,对应自动索引0和1
print(e[1])          #自动索引1,对应自定义索引b
                     #不能混合索引
print(e[:3])         #选取到自动索引3的series

print(' ')
print(b)
print(b[b>b.median()])
print(np.exp(b))
               # 发现操作生成都是series类型


'''判断索引是否在series自定义索引中'''
print('........................................')
print(e)
print('c' in e)
print('g' in e)
print(e.get('g','jeobiden sucks!!!!!!!!!')) 
               # 引用index对应的值，若没有返回后面的内容


'''series之间的操作'''
print(d+e) #相同索引进行运算，不同索引返回NaN; 运算会自动对齐相应索引


'''给series命名、修改数据'''
e.name='make America great again'
print(e)
e['b','c']=999
print(e)



''' 再介绍Dataframe 
纵向索引叫index(axis=0), 横向索引叫column(axis=1)'''
f0=pd.DataFrame(np.arange(10).reshape(2,5))
print(f0)

# 从字典创建dataframe
fd={'one': pd.Series([1,2,3], index=['a','b','c']), 
    'two': pd.Series([4,5,6,7], index=['a','b','c','d'])}
f=pd.DataFrame(fd)
print(f)

print('      ')
print(f.columns) # 显示每一列数据的索引

print('      ')
g=pd.DataFrame(fd, index=['b','c','d'], columns=['two','three'])
print(g)         # 这里的two three锁定了fd中的two列，同时给没有的three填补为NaN
print(g.columns) # 显示每一列数据的索引

fd1={'one': [1,2,3,4], 'two':[9,8,7,6]}
f1=pd.DataFrame(fd1, index=['a','b','c','d'])
print(f1)
print(f1.values) # generate data in f1 in the form of ndarray
print(f1.columns)
print(f1.index)





