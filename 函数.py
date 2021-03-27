# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 05:53:17 2021

@author: Altair
"""

'''函数定义：使用def语句'''
def add1(x):
    x = x + 1
    return x

print(add1(1))



'''例：打印生日歌'''
# 给mike生日歌
def happy():
    print("Happy birthday to you!")
def singMike():
    happy()
    happy()
    print("happy Birthday, dear Mike!")
    happy()
    return " "
print(singMike())

# 或者定义含有参数的函数，使得可以给特定人生日歌
def sing(person):
    happy()
    happy()
    print("Happy birthday, dear", person + "!")
    return " "
print(sing('Zac'))

# 给所有人生日歌，需要定义一个总的函数
def main():
    sing('Mike')
    sing('Zac')
    sing('Lily')
main()



'''计算三角形周长程序'''
import math
def square(x):
    return x*x
def distance(x1, y1, x2, y2):
    dist = math.sqrt(square(x1-x2) + square(y1-y2))
    return dist
def isTriangle(x1, y1, x2, y2, x3, y3):
    flag = ((x1-x2)*(y3-y2)-(x3-x2)*(y1-y2)) !=0
    return flag
def main():
    print("Please enter (x,y) of three points in turn:")
    x1, y1 = eval(input("Point1: (x,y) = "))
    x2, y2 = eval(input("Point2: (x,y) = "))
    x3, y3 = eval(input("Point3: (x,y) = "))
    if(isTriangle(x1, y1, x2, y2, x3, y3)):
        perim = distance(x1, y1, x2, y2) + distance(x2, y2, x3, y3) + distance(x1, y1, x3, y3)
        print("The perimeter is: (0: 0.2f)".format(perim))
    else:
        print("It is not a triangle you mf !!!!!")
main()



'''计算多个账户的总金'''
def addInterest(balances, rate):
    for i in range(len(balances)):
        balances[i] = balances[i]*(1+rate)
def test():
    amounts = [1000, 105, 3500, 739]
    rate = 0.05
    amount = addInterest(amounts, rate)
    print(amounts)
test()
