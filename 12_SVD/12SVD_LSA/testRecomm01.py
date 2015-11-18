# -*- coding: utf-8 -*-
# Filename : testRecomm01.py

from numpy import *
import numpy as np 
import operator
import svdRec2
import matplotlib.pyplot as plt 

eps = 1.0e-6
# 加载修正后数据
Data = svdRec2.loadReData()
dataMat = mat(Data)

# 相似公式：夹角余弦
output1 = svdRec2.recommend(dataMat,2)
print output1

# 相似公式：欧氏距离
output2 = svdRec2.recommend(dataMat,2,simMeas=svdRec2.ecludSim)
print output2

# 相似公式：相关系数
output3 = svdRec2.recommend(dataMat,2,simMeas=svdRec2.pearsSim)
print output3
