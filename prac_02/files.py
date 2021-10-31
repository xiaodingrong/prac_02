"""
作者：Xiaodingrong
日期：2021年10月20日
"""
out_file = open("name txt")
name = input("What is your name?")
print(name, file=out_file)
out_file.close()


in_file = open("numbers.txt")
