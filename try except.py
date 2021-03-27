# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 09:17:55 2021

@author: Altair
"""

'''对输入数字的报错程序，利用try except'''
while True:
    try:
        x=int(input("Please enter a number:"))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again.")
# try后面的语句是尝试运行语句
# 如果尝试运行语句不能运行，则转向except的语句，执行except后面的代码
# ValueError在这里是进行归类、反应的ErrorType



''''除法的运算和报错程序'''
def main():
    try:
        number1, number2=eval(input("Enter two numbers, separated by a coma:"))
        result=number1/number2
    except ZeroDivisionError:
        print("Division by zero!")
    except SyntaxError:
        print("A comma may be missing in the input")
    else:
        print("No exceptions, the results is", result)
    finally:
        print("executing the final clause")
main()
# 一个try可以配多个except子句，捕捉不同的error
# except类似elif



'''运用到之前的解方程程序'''
import math
def main():
    print('This program finds the real solutions to a quadratic\n')
    try:
        a, b, c = eval(input('Please enter the coefficients(a, b, c):'))
        discRoot = math.sqrt(b*b-4*a*c)
        root1 = (-b+ discRoot) / (2*a)
        root2 = (-b- discRoot) / (2*a)
        print("\nThe solutions are:", root1, root2)
    except ValueError as excObj:
        if str(excObj)=="math domain error":
            print("No real roots.")
        else:
            print("You didn't give me the right number of coefficients.")
    except NameError:
        print("\nYou didn't enter three numbers.")
    except TypeError:
        print("\nYour inputs were not all numbers.")
    except SyntaxError:
        print("\nYour input were not all numbers.")
    except:
        print("\nSomething went wrong u muthefucker!")
main()



'''三者最大的程序的三种算法'''
# 通盘比较
# 决策树
# 顺序处理































