# -*- coding: utf-8 -*-
# Filename : 01datingClassTest.py

from numpy import *
import kNN2
import numpy as np 
import matplotlib
import matplotlib.pyplot as plot
import operator
from os import listdir

hoRatio = 0.001      #测试集与训练集的比例
# 加载数据文件
# datingDataMat: 数据集
# datingLabels: 数据分类标签
datingDataMat,datingLabels = kNN2.file2matrix('datingTestSet2.txt') 

# 归一化数据文件
normMat, ranges, minVals = kNN2.autoNorm(datingDataMat)
m = normMat.shape[0] # 数据集行数1000
numTestVecs = int(m*hoRatio)  # 测试集为整个数据集的前1000*0.001个。int转换为整数。
errorCount = 0.0
# print normMat[numTestVecs:m,:] # 训练集，从numTestVecs-->m
# print datingLabels[numTestVecs:m]	# 分类标签集，从numTestVecs-->m

for i in range(numTestVecs):
	  # kNN2.classify：kNN分类器
	  # normMat[i,:]：测试集
	  # normMat[numTestVecs:m,:]：训练集，从numTestVecs-->m
	  # datingLabels[numTestVecs:m]：分类标签集，从numTestVecs-->m
	  # 3 是k值
    classifierResult = kNN2.classify(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
    # classifierResult:分类器所分结果
    # datingLabels[i]:原有分类标签的值
    print ("classifierResult vs datingLabels[i]:%s:%s" %(classifierResult, datingLabels[i]))
    # print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
    # 比较knn分类结果与实际结果的误差
    if (classifierResult != datingLabels[i]): errorCount += 1.0
print "the total error rate is: %f" % (errorCount/float(numTestVecs))
print errorCount