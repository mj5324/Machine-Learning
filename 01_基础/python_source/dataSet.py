# -*- coding: utf-8 -*-
# Filename : dataSet.py

from numpy import *
import operator
import numpy as np 
import matplotlib.pyplot as plt

# 数据集:
# 3.542485	1.977398	-1
# 3.018896	2.556416	-1
# 7.551510	-1.580030	1
# 2.114999	-0.004466	-1
# 8.127113	1.274372	1
# 7.108772	-0.986906	1
# 8.610639	2.046708	1
# 2.326297	0.265213	-1
# 3.634009	1.730537	-1
# 0.341367	-0.894998	-1
# 3.125951	0.293251	-1
# 2.123252	-0.783563	-1
# 0.887835	-2.797792	-1
# 7.139979	-2.329896	1
# 1.696414	-1.212496	-1
#
# dataSet导入
dataMat = []; classLabels = []
fr = open("testSet.txt")
for line in fr.readlines():
    lineArr = line.strip().split()
    dataMat.append([float(lineArr[0]), float(lineArr[1])])
    classLabels.append(int(lineArr[2]))

# 绘制图形
i = 0;
for mydata in dataMat:
	if classLabels[i]==1:
		plt.scatter(mydata[0],mydata[1],c='blue',marker='o')
	if classLabels[i]==-1:
		plt.scatter(mydata[0],mydata[1],c='red',marker='s')	
	i += 1	
plt.show() 