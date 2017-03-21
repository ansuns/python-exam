# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'

#name = input('输入你的姓名:')
#print('Hello,',name)

age = input('输入你的年龄：\n')
age = int(age)
if age<18:
    print('你未成年人了')
elif age <40:
    print('你不是人')
elif age <80:
    print('你的命真长呀')
elif age<100:
    print('你已经成仙了')
else:
    print('你开挂了 吧！！啊啊啊？？')