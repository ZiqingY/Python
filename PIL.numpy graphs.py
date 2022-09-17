# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 21:55:14 2021

@author: Altair
"""

# RGB色彩模式：红绿蓝。那么一个图像就是一个RBG矩阵

from PIL import Image
import numpy as np

# pic=np.array(Image.open(“路径+文件名"))
# print(pic.shape, pic.dtype)
# 输出(xxx, xxx, x) uint8 # 分别是高度、宽度和像素RGB值

######### 以下皆是图像变换例子：#######

#————————————————————————————————————————
# pic1= [255,255,255]-pic
# pic_1=Image.formarray(pic1.astype('unit8'))
# pic_1.save("路径+名称")

#————————————————————————————————————————
# pic=np.array(Image.open("路径+文件名").convert('L'))    #转成灰度图片
# pic2=255-pic
# pic_2=Image.formarray(pic2.astype('uint8'))
# pic_2.save("路径+名称")

#________________________________________
# pic=np.array(Image.open("路径+文件名").convert('L'))    
# pic3=(100/255)@a+150
# pic_3=Image.formarray(pic2.astype('uint8'))
# pic_3.save("路径+名称")

#_________________手绘风格滤镜_____________
# a=np.array(Image.open("路径+文件名").convert('L').astype('float'))
# depth=10
# grad = np.gradient(a)
# grad_x,grad_y=grad
# grad_x = grad_x*depth/100
# grad_y = grad_y*depth/100
# A = np.sqrt(grad_x**2 + grad_y**2 +1.)
# uni_x = grad_x/A
# uni_y = grad_y/A
# uni_z = 1./A
# 
# vec_e1 = np.pi/2.2
# vec_az = np.pi/4
# dx = np.cos(vec_el)*np.cos(vec_az)
# dy = np.cos(vec_el)*np.sin(vec_az)
# dz = np.sin(vec_el)
#
# b=255*(dx*uni_x + dy*uni_y + dz*uni_z)
# b=b.clip(0,255)
# 
# pic_handmade=Image.formarray(b.astype('uint8'))
# pic_handmade.save("路径+名称")


