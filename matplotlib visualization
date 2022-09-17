# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:45:31 2021

@author: Ziqing
"""

# Matplotlib库网站: http://matplotlib.org/gallery.html
# matplotlib.pyplot是命令子库

import numpy as np
import matplotlib.pyplot as plt


'''一维度参数被默认为y轴，x轴为自动生成的索引'''
# list/tuple into graphs
plt.plot([3,1,4,5,2])
plt.ylabel("grade", fontsize=30) # 命名y轴为grade,字体大小
plt.savefig('test',dpi=600) # 保存图像为png格式dpi指定像素
plt.show()



'''确定x轴、y轴'''
plt.plot([0,2,4,6,8],[3,1,4,5,2]) # x值，y值
plt.ylabel("Grade",  fontsize=20) 
plt.axis([-1,10,0,6]) # [x轴始,x轴终，y轴始,y轴终]
plt.show()



'''绘图区域、画多个图''''
# 例：分成3行2列，选取第4块区域
plt.subplot(3,2,4)

# 例：分成2行1列，选取第1块区域，绘制能量衰减曲线
def f(t):
    return np.exp(-t)*np.cos(2*np.pi)
a=np.arange(0.0, 5.0, 0.02)
plt.subplot(2, 1, 1)
plt.plot(a,f(a))
# 选取第2块区域，绘制余弦曲线
plt.subplot(2, 1, 2)
plt.plot(a, np.cos(2*np.pi*a),'r--')
plt.show()



'''画多条曲线： plt.plot(x,y,'format_string', **kwargs)  
**kwargs代表可以放入更多(x,y,format_string), 用来绘制多条曲线'''
a = np.arange(10)
plt.plot(a,a*1.5, a,a*2.5, a,a*3.5, a,a*4.5)
# 画出四条曲线，每一对输入为 自变量,因变量
plt.show()
plt.plot(a,a*1.5,'go-', a,a*2.5,'rx', a,a*3.5,'*', a,a*4.5,'b-.')
# format_string分成颜色字符、风格字符、标记字符
plt.show()



'''添加文本注释'''
b=np.arange(0.0, 5.0, 0.02)
plt.plot(b, np.cos(2*np.pi*b),'r--')          #作出曲线
plt.xlabel('time',fontsize=15, color='green') #x轴标题
plt.ylabel('swing')                           #y轴标题
plt.title(r'sin wave $y=cos(2\pi x)$', fontsize=25)
                                              #图表标题
                                              # r''为排版语法
plt.text(1, 1.5, r'$\mu=100$', fontsize=15)   #注释位置x=1,y=1.5
                                              # \ + greek letter显示希腊字母手写体
                                              # $ sign for absolute quote
plt.annotate(r'$\mu=100$',xy=(2,1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black',shrink=0.1,width=2))
                                              #配注释；加箭头，黑色，与曲线间隔0.1，粗度2
plt.axis([-1,6,-2,2])                         #x,y轴区间
plt.grid(True)                                #显示网格
plt.show()



'''构造复杂子区域'''
import matplotlib.gridspec as gridspec
# 先分成3×3
gs = gridspec.GridSpec(3,3)
# 再确定各个区域：
ax1 = plt.subplot(gs[0,:])     #覆盖第一行行全部
plt.text(0.5, 0.5, r'1', fontsize=15)

ax2 = plt.subplot(gs[1, 0:-1]) #覆盖第二行0到-1块
plt.text(0.5, 0.5, r'2', fontsize=15)

ax3 = plt.subplot(gs[1:, -1])  #覆盖从第一行开始所有行，在-1列
plt.text(0.5, 0.5, r'3', fontsize=15)

ax4 = plt.subplot(gs[2, 0])    #三行一列的块
plt.text(0.5, 0.5, r'4', fontsize=15)

ax5 = plt.subplot(gs[2, 1])    #三行二列的块
plt.text(0.5, 0.5, r'5', fontsize=15)



































