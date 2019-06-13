#! /bin/python
#! coding:utf-8
from __future__ import division

import requests
# #上面一句代码就可以让python的注释里可以含有中文
# 
# #liunx中可能默认安装了python，所以在bash中直接敲下python即可进入到python的界面（额..............）
# 
#1.变量和赋值
a = 3.14
counter = 1000
name = "hzq"
kilometers = 1.609 * counter


print a
print counter
print name
print kilometers
# 
# n = 2
# n = n * 10
# print n
# 
# a = 100
# print a
# print type(a)
# 
# a = "hehe"
# print a
# #print type(a）#不能查看字符串的类型				
# 
# a = 100000000000
# a = a **5
# print a
# 
# #认识复数
# a = 10 + 5j
# print a
# print type(a)
# 
# #认识字符串
# a = 'heh'
# a = "heheh"
# a = '''heheheh'''
# print a
# 
# a = ''''I' say "hah",\nyou say 'heh' ''' #后面的三引号不能与单引号靠近
# print a
# 
# a = 'abcd'
# print a[1:-1]
# print a[:-1]
# print a[1:]
# print a[:]
# print a
# b = a * 4
# print b
# print type(b[0])
# print len(b)
# 
# b = 100
# print "b = %d" %b
# 
# a = True   #注意，第一个字母是大写的
# print a
# print type(a)
# 
# b = a + 1
# print b
# 
# 
# #print函数是将结果输出到标准输出（显示器）上
# #raw_input函数是从标准输入中获取用户输入
# #name = raw_input("enter name:")
# #print name
# 
# #raw_input返回的结果十一个字符串，如果需要获得数字，需要用int函数吧字符串转换成数字
# #num = raw_input('enter number:')
# #print type(num)
# #num = (int)num + 1                                                                          #出错
# #print type(num)
# #print (int)num + 1                                                                            #出错
# 
# 
# #认识python上+ - * / %    // **运算符
# a = 1
# b = 2
# print a / b
# print a//b  #地板除
# 
# a = 1.0
# b = 2
# print a/b
# print a//b  #地板除
# 
# #使用from __future__ import division就会使/变成精确除法
# #from __future__ import division  #must occur at the beginning of the file
# a = 1
# b = 2
# print a/b
# 
# a = 100
# b = 100
# print a**b
# 
# #python也支持> >= == < <= !=这些比较运算符，结果十一个bool值
# #还支持逻辑运算符and not or
# print 2 < 4 and 2 == 4
# 
# print not 6.2 <= 6
# 
# print 'hah' == 'hhe'
# 
# 
# #认识列表/元组/字典
# alist = [1,2,'heh']
# print type(alist)
# print alist
# 
# atuple = (1,2,3,3,'heh')
# print type(atuple)
# print atuple
# #列表和元组唯一的区别就是：列表中的元素可以修改，而元组的不行
# 
# a = {'insert':1,'empty':2}
# print type(a)
# print a
# 

