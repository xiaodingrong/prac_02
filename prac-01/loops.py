# -*- coding:utf-8 -*-
"""
作者：xiaodingrong
日期：2021年10月19日
"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a.  count in 10s from 0 to 100: `0 10 20 30 40 50 60 70 80 90 100
for number in range(0, 101, 10):
    print(number, end=" ")
#b.  count down from 20 to 1: `20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1`
for number in range(20, 0, -1):
    print(number, end=" ")
"""
 c.  print n stars. Ask the user for a number, then print that many stars
        (*), all on one line  
        *Note: this is a very simple loop for repeating n times. We use for
        loops for "definite" iteration like this. while loops are used for
        "indefinite" iteration (like repeating while a user input is
        incorrect).*  
        Sample output:
        
        Number of stars: 4
        ****
"""
get_number = int(input("Please input a number: "))
for star in range(0, get_number):
    print("*", end="")

"""
 d.  print n lines of increasing stars. Using the same number as above
        print lines of increasing stars, starting at 1. E.g. if **4** was
        the number entered, your single loop should print

"""
get_number = int(input("Please input a number: "))
for column in range(0,get_number):
    for rank in range(0, column+1):
        print("*", end="")
    print("")