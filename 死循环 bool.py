# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:27:19 2021

@author: Altair
"""


'''死循环用来捕捉输入异常'''
while True:
    try:
        x = int(input("Please enter a number:"))
        break
    except ValueError:
        print("That was not valid number you motherfucker!")



'''直到输入满足结束循环条件为止 发出警示'''
number = -1
while number < 0:
    number = eval(input("Enter a positive number:"))
    if number < 0:
        print("The number ypu entered is not positive mf!")
# 直接进入循环，一开始没有输入



'''用break实现直到输入满足结束循环条件为止 发出警示'''
while True:
    number = eval(input("Enter a positive number:"))
    if number >= 0:
        break
    else:
        print("The number ypu entered is not positive mf!")
        
        
        
'''bool表达式 用于条件语句'''
scoreA = 0
scoreB = 0
while not (scoreA == 15 or scoreB == 15):
# 或者 (not scoreA==15) and (not scoreB==15)
# 或   scoreA !=15 and coreB!=15
    print("Match continues")
    break

scoreA1 = 7
scoreB1 = 0
while (scoreA1 == 15 or scoreB1 == 15) or (scoreA1==7 and scoreB1==0) or (scoreA1==0 and scoreB1==7):
    print("Match ends")
    break



'''bool表达式默认空为False'''
ans = input("What fodd u wanna have for dinner?")
food = ans or "shit"
print(food)
