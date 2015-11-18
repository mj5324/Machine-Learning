# -*- coding: utf-8 -*-
# Filename : testSvd01.py

from numpy import *
import numpy as np 
import operator
import svdRec2
import matplotlib.pyplot as plt 

eps = 1.0e-6
# numpy求矩阵的奇异分解
# U:酉矩阵
# Sigma:半正定m×n阶对角矩阵
# VT:V的共轭转置
U,Sigma,VT = linalg.svd([[1,1],[7,7]])
# print "U:",U
# print "Sigma:",Sigma
# print "VT:",VT

# 矩阵相似形验证
Data = svdRec2.loadExData()
# 数据矩阵化
Data = mat(Data)
print "Data:\n",Data
# 进行奇异值分解
U,Sigma,VT = linalg.svd(Data)
# 只取前3项重构相似阵
Sig3 = mat(Sigma[:3]*eye(3))
U3 = U[:,:3] 
VT3 = VT[:3,:]
# D3 == Data 矩阵是相似的 
D3 = U3*Sig3*VT3
# 返回D3中大于0的所有元素的下标
indxs = nonzero(abs(D3.A)<eps)
D3[indxs]=0
# 输出D3
# print "D3:\n", D3
D_D3 = Data-D3
# 返回Data-D3中大于0的所有元素的下标
idxs = nonzero(abs(D_D3.A)<eps)
D_D3[idxs]=0
# print "如果输出为全零矩阵，Data与D3两矩阵相似",D_D3

# SVD变换
Data = svdRec2.loadReData()
DataMat = mat(Data)

# 奇异值分解
U,Sigma,VT = linalg.svd(Data)
SigmaE = mat(Sigma[:4]*eye(4))
# VT的转置:V1是dataMat的相似矩阵
V1 = VT.T[:,:4]
print "V1:\n",V1
# 验证相似性
V2 = DataMat.T*U[:,:4]*SigmaE.I
print "V2:\n",V2
V1_V2 = V1-V2
idxs = nonzero(abs(V1_V2.A)<eps)
V1_V2[idxs] =0
print "V1-V2:\n", V1_V2[idxs]
