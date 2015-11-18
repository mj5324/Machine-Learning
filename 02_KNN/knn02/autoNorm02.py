# -*- coding: utf-8 -*-
# Filename : autoNorm02.py

from numpy import *
import operator
import numpy as np 
import matplotlib
import matplotlib.pyplot as plot

# 数据集归一化
dataSet = array([[4,0.10],[3,0.15],[2,0.13],[1,0.2]])
print "dataSet:",dataSet
print
# 返回数据集的最小值矩阵，按列区分，返回每一列的最小值
minVals = dataSet.min(0)
print "minVals:",minVals
print
# 返回数据集的最大值矩阵，按列区分，返回每一列的最大值
maxVals = dataSet.max(0)
print "maxVals:", maxVals
print
# 返回最大值矩阵-最小值矩阵的范围差
ranges = maxVals - minVals
print "ranges:", ranges
print
# shape(dataSet):返回一个向量：矩阵的行与列的数量 4,2
# zeros(shape(dataSet)):初始化 normDataSet 为与dataSet相同的全零矩阵
normDataSet = zeros(shape(dataSet))

# 初始化 normDataSet 为与dataSet相同的零矩阵
m = dataSet.shape[0]  # dataSet的行数

# 以最小值填充矩阵 tile(minVals, (m,1))
print "tile(minVals, (m,1)):",tile(minVals, (m,1))
print
# 原始数据集(dataSet)-最小值构成的矩阵
normDataSet = dataSet - tile(minVals, (m,1))
print ("dataSet - tile(minVals, (m,1)):\n%s" %normDataSet) 
print
# 线性归一化公式：(x-MinValue)/(MaxValue-MinValue)
# 矩阵各元素除以范围值的矩阵
normDataSet = normDataSet/tile(ranges, (m,1))   #两矩阵逐个元素相除
print ("normDataSet/tile(ranges, (m,1)):\n%s" %normDataSet) 
print
# return normDataSet, ranges, minVals