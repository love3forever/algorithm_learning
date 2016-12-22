#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-22 16:03:54
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$


def quickSort(seq):
    if seq == []:
        return []
    first = seq[0]
    lesser = filter(lambda x: x <= first, seq[1:])
    greater = filter(lambda x: x > first, seq[1:])
    return quickSort(lesser) + [first] + quickSort(greater)
