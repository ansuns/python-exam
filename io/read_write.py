#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'

#如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在：
'''
Traceback (most recent call last):
  File "read_write.py", line 5, in <module>
    f = open('./pythxon.txt', 'r')
FileNotFoundError: [Errno 2] No such file or directory: './pythxon.txt'

'''
#果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示：
#每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法:
'''
try:
    f = open('./python.txt', 'r')
    content = str(f.read())
    print(content)
finally:
    if f:
        f.close()
'''

with open('./python.txt', 'r') as f:
    print(f.read())
#这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。


#二进制文件
#读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
'''
f = open('./test.jpg', 'rb')
print(f.read())
f.close()
'''


#写文件
with open('./python.txt', 'w') as f:
    f.write('Hello World again!!')

