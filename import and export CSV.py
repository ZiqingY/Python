# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 17:46:53 2021

@author: Altair
"""

'''导入、输出一维数据CSV文件'''
# 输出语法：np.savetxt(frame, array, fmt='%.18e', delimiter=None)
# 导入语法：np.loadtxt(frame, dtype=np.float, delimiter=None, unpack=False)
import numpy as np
a=np.arange(100).reshape(5,20)



'''输出'''
np.savetxt('导入输出CSV文件a.csv', a, fmt='%d', delimiter=',')     # %d为整数形式
np.savetxt('导入输出CSV文件a1.csv', a, fmt='%.1f', delimiter=',')  # %.1f为一位小数的float



'''导入'''
b=np.loadtxt('导入输出CSV文件a1.csv', delimiter=',')
print(b)
c=np.loadtxt('导入输出CSV文件a1.csv', dtype=np.int, delimiter=',')  # 读入后元素为整数类型，unpack为False意味着读成一个数组
print(c)



'''导入、存取多维数据CSV文件'''
# 输出语法：a.tofile(frame, sep='', format='%s')
# 导入语法：np.fromfile(frame, dtype=float, count=-1, sep='')

d=np.arange(100).reshape(5,10,2)
d.tofile('多维d.dat', sep=',', format='%d')                        # 不指定sep的话会读成二进制文件
e = np.fromfile('多维d.dat', dtype=np.int, sep=',')                # count为读入元素个数，默认为-1，读入整个文件
print(e)                                                           # 发现维度丢失，需要reshape
e1 = np.fromfile('多维d.dat', dtype=np.int, sep=',').reshape(5,10,2) # 规定读入格式



''' 便捷文件存取方法,可以保存维度信息'''
# 输出语法：np.save(frame, array)
# 导入语法：np.load(frame)
np.save('多维d1',d)
f=np.load('多维d1.npy')
print(f)                                                          # 发现保留维度
