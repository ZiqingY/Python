# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:45:12 2021

@author: Altair
"""

import numpy as np
import matplotlib.pyplot as plt

'''常用图表语法
plt.plot(x,y,fmt,...) 坐标系
plt.boxplot(data,notch,position) 箱形图
plt.bar(left,height,width,bottom) 条形图
plt.barh(width,bottom,left,height) 横向条形图
plt.polar(theta,r) 极坐标图
plt.pie(data,explode) 饼图
plt.psd(x, NFFT=256, pad_to, Fs) 功率谱密度图
plt.specgram(x, NFFT=256, pad_to, F) 谱图
plt.cohere(x,y, NFFT=256, Fs) X-Y相关性函数
plt.scatter(x,y) 散点图
plt.step(x,y,where) 步阶图
plt.hist(x,bins,normed) 直方图
plt.contour(X,Y,Z,N) 等值图
plt.vlines() 垂直图
plt.stem(x,y,linefmt,markerfmt) 柴火图
plt.plot_date() 数据日期
'''



'''扇形图（例）'''
nutrition = 'Protein','Carbs','Fat','Micronurtient' #饼组成成分
sz = [33, 33, 25, 9]                                #各区域相对大小
expl = (0.1, 0, 0, 0)                               #各区域膨出程度
plt.pie(sz, explode=expl, labels=nutrition, autopct='%1.1f%%',shadow=True, startangle=90)
                                                    #把以上三个参数代入饼图函数
                                                    #autopct为百分比显示形式，startangle为饼旋转角度
plt.axis('equal')                                   #让饼图摆正
plt.show()




'''直方图例子'''
mu, sigma=100, 20
a = np.random.normal(mu, sigma, size=100)
plt.hist(a, 10, histtype='stepfilled', facecolor='b', alpha=0.5)
                                                    # a后面的参数bins表示直方的个数是多少
                                                    # alpha为直方颜色深浅
plt.title('Histogram')
plt.show()



'''极坐标图例子'''
N=20                                 # 绘制极坐标数量 
theta = np.linspace(0.0, 2*np.pi, N, endpoint=False)
                                     # 平均分配每个极坐标的对应角度
radii = 10 * np.random.rand(N)
width = np.pi / 4*np.random.rand(N)
ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, width=width, bottom=0.0) 
                                     # 生成极坐标
                                     # radii和width的地方分别是极坐标的height参数和width参数
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r/10.))
    bar.set_alpha(0.5)
                                     # 对极坐标颜色进行设定
plt.show()



'''散点图例子'''
fig, ax = plt.subplots()                # 生成绘制区域, subplots默认区域数量为1
ax.plot(10*np.random.randn(100), 10*np.random.randn(100), 'o') 
                                        # 在绘图区域ax内作散点.参数: (x,y,点形状)
ax.set_title('Simple Scatter')
plt.show()








