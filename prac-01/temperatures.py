# -*- coding:utf-8 -*-
"""
作者：xiaodingrong
日期：2021年10月21日
"""
get_number = int(input("Please input a number: "))
for column in range(0,get_number):
    for rank in range(0,column+1):
        print("*",end="")
    print("")