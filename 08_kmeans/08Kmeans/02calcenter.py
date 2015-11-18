# -*- coding: utf-8 -*-
# Filename : 01DateSet.py

from numpy import *
import numpy as np 
import operator
import kMeans2
import matplotlib.pyplot as plt 

# 导入数据集
# 将格式转换为矩阵
dataMat = [] 
fr = open("testSet.txt")
for line in fr.readlines():
    curLine = line.strip().split('\t')
    fltLine = map(float,curLine) # map all elements to float()
    dataMat.append(fltLine)
    
dataMat = mat(dataMat) # 转换为numpy矩阵

# 计算中心
k = 4 # 外部指定的聚类数
n = shape(dataMat)[1] # 返回dataMat的列数:2
# 初始化聚类中心矩阵:k*n 
centroids = mat(zeros((k,n)))
# 创建随机聚类中心 
for j in range(n):
    minJ = min(dataMat[:,j]) # 返回第j列的最小值
    maxJ = max(dataMat[:,j]) # 返回第j列的最大值 	
    rangeJ = float(maxJ - minJ) # 范围：返回第j列最大值与最小值的差
    # random.rand(m,n):产生一个0~1之间的随机数，
    # m,n表示产生m行n列的随机数
    # 计算第j列的中心: j列最小值 + 范围值*随机数(0~1)
    centroids[:,j] = mat(minJ + rangeJ * random.rand(k,1))
print centroids

# 计算向量的欧式距离:
for dataLine in dataMat:
	distance = sqrt(sum(power(dataLine - centroids[0], 2))) #
print distance

	