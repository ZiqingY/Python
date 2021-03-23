# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 05:08:38 2021

@author: Altair
"""
# 设计温度单位转换的运算
val=input("请输入带温度表示符号的温度值（例如32C）：")
if val[-1] in ['C','c']:
    f = 1.8 * float(val[0:-1]) + 32  # val[0:-1]为val的1~倒数第二个值
                                     # float()函数将括号内转化为可进行运算的小数
    print("转换后的温度为: %.2fF" % f) # %.2f代表两位小数的浮点数，F为单位
                                     # %选择要输出的变量，这里变量为f
elif val[-1] in ['F','f']:
    c = (float(val[0:-1]) -32) / 1.8
    print("转换后的温度为： %.2fC" % c) 
else:
    print("输入有误")
    

# 例：输入输出运算
num1 = input("The first number is")
num2 = input("The second number is")
avg_num = (float(num1) + float(num2)) / 2
print("The average number is %f" % avg_num)


# 例：绘制蟒蛇
import turtle
def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)  #让乌龟按照圆形轨迹运行，rad为圆形半径位置，angle为弧度值
        turtle.circle(-rad, angle)
    turtle.cicle(rad, angle/2)
    turtle.fd(rad)                 #让乌龟向前直线爬行，参数为爬行的距离
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad*2/3)
    
def main():
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 30
    turtle.pensize(pythonsize) #乌龟运行轨迹的宽度
    turtle.pencolor("blue")    #乌龟运行轨迹的颜色
    turtle.seth(-40)           #乌龟运行的方向
    drawSnake(40, 80, 5, pythonsize/2)

main()



