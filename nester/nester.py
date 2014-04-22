# -* - coding:UTF-8 -* -
"""这是“nester.py”模块，提供了一个名为print_lol()的函数"""
# 这个函数用来打印表中表的递归程序
"""This is the multiple lines of comments
   输出表中表的元素的递归程序"""
import sys

def print_lol(the_list, indent=False, level=0, fn=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fn)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=fn)
            print (each_item, file=fn)
