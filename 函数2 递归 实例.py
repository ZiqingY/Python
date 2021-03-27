# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 05:53:19 2021

@author: Altair
"""

'''输入本金、利息展示十年总金增长的图表'''
def caculationNum(principal):
    total= int(principal*4/1000.0)
    return total
# 将本金换算成￥数
def createTable(principal, apr):
    for year in range(1, 11):
        principal = principal*(1+apr)
        print("%2d"%year, end = '')
        total = caculationNum(principal)
        print("￥"*total)
    print("0.0K    2.5K    5.0K    7.5K    10.0K")
# 将利息代入计算，作图
def main():
    print("This program plots the growth of a 10-year investment.")
    principal=eval(input("Enter the initial principal:"))
    apr = eval(input("Enter the annualized interest rate:"))
    createTable(principal, apr)
main()



'''递归函数之阶乘'''
def facturial(n):
    if n == 0:
        return 1
    else:
        return n*facturial(n-1)
print(facturial(5))



'''递归之字符反转'''
def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]
    # 将一个个字母往最后移
print(reverse('ziqing yan'))






