#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'

'''
break

在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：

n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')
上面的代码可以打印出1~100。

如果要提前结束循环，可以用break语句：

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
执行上面的代码可以看到，打印出1~10后，紧接着打印END，程序结束。

可见break的作用是提前结束循环。

continue

在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。

n = 0
while n < 10:
    n = n + 1
    print(n)
上面的程序可以打印出1～10。但是，如果我们想只打印奇数，可以用continue语句跳过某些循环：

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
执行上面的代码可以看到，打印的不再是1～10，而是1，3，5，7，9。

可见continue的作用是提前结束本轮循环，并直接开始下一轮循环。
可见continue的作用是提前结束本轮循环，并直接开始下一轮循环。
'''
n = 0
while n < 10:
    n = n + 1
    print(n)
print('END')
l = 0
while l < 10:
    l = l + 1
    if l % 2 != 0:
        continue
    print(l)
print('END')