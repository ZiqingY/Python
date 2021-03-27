# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 08:15:47 2021

@author: Altair
"""

'''用for语句设计均值程序'''
n = eval(input("How many numbers?"))
sum = 0.0
for i in range(n):
    x = eval(input("Enter a number >>"))
    sum = sum+x
print("\nThe average is", sum/n)



'''用for/while结合else, break计算累加和'''
sum=0
number=0
while number<20:
    number += 1
    sum += number
    if sum > 100:
        break
print("The starting number is", number)
print("The sum is", sum)
# 当sum>100时，终止while的循环，执行下面的语句(print...)，即生成此时的number和sum值



'''for/while结合continue'''
for num in range(2,10):
    if num %2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
# num%2==0说明num是偶数
# continue只是停止当前循环，不执行下面语句，回到上面的if再来(还在for loop的大框架下)
# 若if不成立，那么就执行print("Found an odd number", num)



'''设计程序：输出2到9的素数和非素数'''
for n in range(2,10):
    for x in range(2,n):
        if n % x ==0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
# n循环:2, 3, 4,...,10
  # x循环:2, 3, 4, ...,n
# 这里的break终止的是x的循环