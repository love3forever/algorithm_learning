#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-22 15:55:54
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

# 二分查找
from random import choice
from generat_list import creatList
from quick_sort import quickSort


def halfIntervalSearch(start, end, value, seq):
    while start <= end:
        mid = (start + end) / 2
        print('start moves to:{},end moves to:{},mid moves to:{}'.format(
            start, end, mid))
        if seq[mid] == value:
            return mid
        elif seq[mid] > value:
            end = mid - 1
        elif seq[mid] < value:
            start = mid + 1
    return -1

if __name__ == '__main__':
    data = creatList(10)
    print('unsorted list:{}'.format(data))
    data = quickSort(data)
    print('sorted list:{}'.format(data))
    target = choice(data)
    print('target value:{}'.format(target))
    start = 0
    end = len(data) - 1
    mid = halfIntervalSearch(start, end, target, data)
    print('the value index is : {}'.format(mid))
