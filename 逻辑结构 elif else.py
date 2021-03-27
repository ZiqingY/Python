# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 07:29:39 2021

@author: Altair
"""

'''另一个if IPO例子：空气质量评估程序'''
def main():
    PM = eval(input("What is today's PM2.5?"))
    if PM>75:
        print("Unhealthy. Be careful!")
    if PM<35:
        print('Good. Go running!')
main()



'''求解二次方程的程序，用if else'''
import math
def main():
    print('This program finds the real solutions to a quadratic\n')
    a, b, c = eval(input('Please enter the coefficients(a, b, c):'))
    delta = b*b-4*a*c
    if delta<0:
        print("\nThe equation has no real roots!")
    else:
        if delta==0
           x=-b/(2*a)
           print("There is a double root at", x)
        else:
           discRoot = math.sqrt(b*b-4*a*c)
           root1 = (-b+ discRoot) / (2*a)
           root2 = (-b- discRoot) / (2*a)
           print("\nThe solutions are:", root1, root2)
main()
# 注：要输入(a,b,c)的形式



'''同样的程序，使用elif'''
def main():
    print('This program finds the real solutions to a quadratic\n')
    a, b, c = eval(input('Please enter the coefficients(a, b, c):'))
    delta = b*b-4*a*c
    if a==0:
        x=-b/c
        print("\nThere is an solution", x)
    elif delta==0:
        x=-b/(2*a)
        print("There is a double root at", x)
    elif delta<0:
        print("\nThe equation has no real roots!")
    else:
        discRoot = math.sqrt(b*b-4*a*c)
        root1 = (-b+ discRoot) / (2*a)
        root2 = (-b- discRoot) / (2*a)
        print("\nThe solutions are:", root1, root2)
main()
# elif与if互斥，但功能并列



'''空气质量评估程序，利用elif'''
def main():
    PM=eval(input("What is today's PM2.5?"))
    if PM<35:
        print("Good. Go running!")
    elif PM<75:
        print("Modetrate. Go walking!")
    elif PM<115:
        print("Unhealthy for sensitive group!")
    elif PM<150:
        print("Unhealthy.Limited prolonged exertion!")
    elif PM<250:
        print("Very Unhealthy. Avoid prolonged exertion!")
    else:
        print('Hazardous. Remain INDOORS!')
main()







