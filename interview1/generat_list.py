#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-22 15:57:31
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

# 用以生成随机序列
from random import randint


def creatList(num):
    return [randint(1, num * num) for x in range(num)]
