# -*- coding:utf-8 -*-
"""
作者：Xiaodingrong
日期：2021年10月19日
"""
"""
A shop requires a small program that would allow them to quickly work
out the total price for a number of items, each with different prices.

The program allows the user to enter the number of items and the price
of each different item.  
Then the program computes and displays the total price of those items.  
If the total price is over $100, then a 10% discount is applied to that
total before the amount is displayed on the screen.

The output should look something like (**bold text** represents user
input):

"""

total = 0
number = int(input("Please input the number of item"))
for i in range(number):
    price = float(input("number of item"))
    total += price

if total > 100:
    total = total*0.9

print("Total price for{} item is {:.2f}".format(number, total))





