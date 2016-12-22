#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-22 16:49:29
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

# 将一个列表中的所元素分别打印出来


def outPut(f):
    def printData(data):
        result = f(data)
        for item in result:
            print(item)
    return printData


@outPut
def getList(data):
    if not data or data == []:
        pass
    for item in data:
        if isinstance(item, list):
            getList(item)
        elif item:
            yield item


if __name__ == '__main__':
    data = [1, [2, [3, []]], [], [1, 2, 3, 4]]
    getList(data)
