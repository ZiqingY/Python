# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 17:46:53 2021

@author: Altair
"""

#___________导入、输出CSV文件____________________
import numpy as np
a=np.arange(100).reshape(5,20)
# 输出
np.savetxt('导入输出CSV文件a.csv', a, fmt='%d', delimiter=',')
np.savetxt('导入输出CSV文件a1.csv', a, fmt='%1f', delimiter=',')


# 导入
b=np.loadtxt('导入输出CSV文件a1.csv', delimiter=',')
print(b)

c=np.loadtxt('导入输出CSV文件a1.csv', dtype=np.int, delimiter=',')
print(c)



# 多维数据的导入和存取
d=np.arange(100).reshape(5,10,2)
d.tofile('多维d.dat', sep=',', format='%d')
# 不指定sep的话会生成二进制文件

e = np.fromfile('多维d.dat', dtype=np.int, sep=',')
print(e) # 发现维度丢失，需要reshape



# 便捷文件存取,可以保存维度信息
np.save('多维d1',d)

f=np.load('多维d1.npy')
print(f) # 发现保留维度