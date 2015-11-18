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
    
dataMat = mat(dataMat) #转换为numpy矩阵
for cent in dataMat:
	plt.scatter(cent[0,0],cent[0,1],s=60,c='blue',marker='o')
plt.show() 	


	

	