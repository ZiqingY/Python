# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 12:57:25 2021

@author: Altair
"""

'''允许用户随时停止的交互式循环'''
def main():
    sum = 0.0
    count = 0
    moredata = 'yes'
    while moredata[0] == 'y':
        x = eval(input('Enter a number>>'))
        sum = sum + x
        count = count + 1
        moredata = input('Do you have more numbers (yes or no)')
    print("\nThe average of the numbers is", sum/count)
main()
# 这里利用moredata的首字母是否为y来作为while条件



'''通过input本身来作为终止循环的signal'''
def main():
    sum = 0.0
    count = 0
    x = eval(input("Enter a number (negative to quit) >>"))
    while x >= 0:
        sum =sum + x
        count = count + 1
        x = eval(input("Enter a number (negative to quit)>>"))
    print("\n The average of the number is",sum/count)
main()
# 但是不能求含有负数的平均值



'''允许任何数字计算均值的signal循环'''
def main():
    sum = 0.0
    count = 0
    xStr = input("Enter a number (<Enter> to quit) >>")
    while xStr != "":
        x = eval(xStr)
        sum = sum + x
        count = count + 1
        xStr = input("Enter a number (<Enter> to quit)>>")
    print("\n The average of the number is",sum/count)
main()
# while条件为 当xStr为空时，即input为空，也就是按回车执行while外语句



'''一行一个数据的文本文件代入循环'''
def main():
    fileName = input("What file are the numbers in?")
    infile = open(fileName, 'r')
    sum = 0
    count = 0
    for line in infile:
        sum = sum + eval(line)
        count = count + 1
    print("\nThe average of the numbers is", sum/count)
main()



'''将文件数据转化成Python字符串数据，代入循环
line = infile.readline()
while line !="":
    line = infile.readline()'''
# 注：换行符不是空符，不影响循环
# readline()函数将文本数据读成python字符串数据
def main():
    fileName = input("What file are the numbers in?")
    infile = open(fileName, 'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line !="":
        sum = sum + eval(line)
        count = count + 1
        line = infile.readline()
    print("\nThe average of the numbers is", sum/count)
main()



'''逗号相隔数据的文本文件 代入循环'''
def main():
    fileName = input("What file are the numbers in?")
    infile = open(fileName, 'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line !="":
        for xStr in line.split(","):
            sum =  sum + eval(xStr)
            count = count + 1
        line = infile.readline()
    print("\nThe average of the numbers is", sum/count)
main()
# 也就是在while循环内又进行了一个循环——计算逗号隔开的值的和



