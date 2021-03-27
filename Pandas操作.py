# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:15:59 2021

@author: Altair
"""

import pandas as pd

d1={'城市':['Beijing','Shanghai','Guangzhou','Shenzhen','Shenyang'],
    '环比':[101.5, 101.2, 101.3, 102.0, 100.1],
    '同比':[120.7, 127.3, 119.4, 140.9, 101.4],
    '定基':[121.4, 127.8, 120.0, 145.5, 101.6]}
print(d1)

d=pd.DataFrame(d1, index=['c1','c2','c3','c4','c5'])
print(d)
print('上海的同比:',d['同比']['c2'])
print(d['同比'][:])
#### 缺失：调出一行Series的代码 #####

# rearrange order of rows:
d=d.reindex(index=['c2','c1','c3','c4','c5'])
print(d)

# rearrange order of columns:
d=d.reindex(columns=['环比','城市','同比','定基'])
print(d)

# 增加新列
high=d.columns.insert(4,'house price')           # 定义新列(4表示添加在4位置的列) 
newd=d.reindex(columns=high, fill_value='high')  # fillvalue填充缺失值
print(newd)

# 删除列、增加新行
nc=newd.columns.delete(0)
ni=newd.index.insert(5,'c0')
nd=newd.reindex(index=ni, columns=nc).ffill()    # 按照上面一行填充c0
print(nd)

# 删除索引（行、列）
ndd=nd.drop(['c0','c5'])
print(ndd)
nddd=nd.drop('同比',axis=1) # 删除的索引轴为1索引轴，而非0索引轴，默认为0索引轴
print(nddd)


# 对索引操作：
# .append(idx)  .diff(idx)  .intersection(idx)  .union(idx)  .delete(loc)  .insert(loc,cn)
da = d.reindex(index=['c5','c4','c3','c2','c1'])
daa = da.reindex(columns=['城市','同比','环比','定基'])
print(daa)
nc=daa.columns.delete(2)
ni=daa.index.insert(5, 'c0')
print(nc) # 去掉'环比'以后的columns
print(ni) # 加上'c0'以后的index
na=daa.reindex(index=ni, columns=nc, fill_value='Nanjing') 
          # 新的columns和index组成新的DataFrame并填充
print(na)




