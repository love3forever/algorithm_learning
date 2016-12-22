#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-22 16:14:38
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

# 通过两个栈构造一个队列


class GenerateList(object):
    """docstring for GenerateList"""

    def __init__(self, s1, s2):
        self._s1 = s1
        self._s2 = s2

    def push(self, data):
        self._s1.append(data)
        print('{} pushed in'.format(data))

    def pop(self):
        if self._s2:
            return self._s2.pop()
        else:
            while self._s1:
                self._s2.append(self._s1.pop())
            if self._s2:
                return self._s2.pop()
            else:
                return 'this is a empty list'


if __name__ == '__main__':
    d1 = list()
    d2 = list()

    clist = GenerateList(d1, d2)
    clist.push(1)
    clist.push(2)
    print(clist.pop())

    clist.push(3)
    print(clist.pop())
    print(clist.pop())
    print(clist.pop())
