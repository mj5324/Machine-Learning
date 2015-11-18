# -*- coding: utf-8 -*-
# Filename : vect_distance.py

from numpy import *
import numpy.linalg
import operator
import matplotlib.pyplot as plot
import scipy.spatial.distance as dist

# 向量
vect1 = mat([1,2,3]); vect2 = mat([6,5,4])

#----各种距离公式----#
# 欧式距离: distO = sqrt( (x1-x2)^2+(y1-y2)^2+(z1-z2)^2 )
pw2V = power(vect1-vect2,2)
distO = sqrt(sum(pw2V))
print "disO:",distO
print
# 标准化欧式距离:
# 统计向量的标准化
meanV1 = mean(vect1); 
stdV1 = std(vect1);
m1 = ones((1,len(vect1)))*meanV1 
if stdV1!=0:
	newVect1 = (vect1-m1)/stdV1 
else: newVect1 = (vect1-m1)
meanV2 = mean(vect2); 
stdV2 = std(vect2); 
m2 = ones((1,len(vect2)))*meanV2 
if stdV2!=0: 
	newVect2 = (vect2-m2)/stdV2 
else: newVect2 = (vect2-m2)
	
pw2V = power(newVect1-newVect2,2)
stddistO = sqrt(sum(pw2V))
print "stddisO:",stddistO
print

# 曼哈顿距离(Manhattan Distance):d(i,j)=|xi-xj|+|yi-yj|
b1 = mat([0,0]);b2=mat([1,0]);b3=mat([0,2])
disM = [sum(abs(b1-b2)),sum(abs(b1-b3)),sum(abs(b3-b2))]
print "disM:",disM
print

# 切比雪夫距离
b1 = mat([0,0]);b2=mat([1,0]);b3=mat([0,2])
disCh = [abs(b1-b2).max(),abs(b1-b3).max(),abs(b3-b2).max()]
print "disCh:",disCh
print

# nonzero
# 海明距离:比较两个串的相似度
# str1 = [1,1,1,0,0];str2 = [0,1,0,1,0]
str1 = mat([1,1,1,0,0]);str2 = mat([0,1,0,1,0])
disH = 0;
# 标准的方法
# for i in range(len(str1)):
# 	if str1[i]!=str2[i]: disH += 1
# numpy 提供的快速计算
# 返回相同字串的索引向量
smstr = nonzero((str1-str2)!=0)[0];
disH = shape(smstr)[1]
print "disH:",disH		 
print

# 马氏距离
# b1 = mat([1,0]) ;b2 = mat([1,1.732]) ; b3 = mat([-1,0])
X = mat([[1,2],[1,3],[2,2],[3,1]])
Y = dist.pdist(X,'mahalanobis',VI=None)
print "dist.mahalanobis:",Y

#夹角余弦(Cosine)公式: 计算空间内两点之间的夹角余弦
b1 = mat([1,0]) ;b2 = mat([1,1.732]) ; b3 = mat([-1,0])
cosb12 = sum(b1*b2.T)/(sqrt(sum(power(b1,2)))*sqrt(sum(power(b2,2))))
cosb13 = sum(b1*b3.T)/(sqrt(sum(power(b1,2)))*sqrt(sum(power(b3,2))))
cosb23 = sum(b2*b3.T)/(sqrt(sum(power(b2,2)))*sqrt(sum(power(b3,2))))
print "cosb12:",cosb12,"  cosb13:",cosb13,"   cosb23:",cosb23
print

# 相关系数
vect1 = mat([1, 2 ,3 ,4 ]); vect2 = mat([3 ,8 ,7 ,6])
# 相关系数(Correlation coefficient):衡量X与Y线性相关程度,其绝对值越大,则表明X与Y相关度越高。
# 相关系数取值为1（正线性相关）或-1（负线性相关）
mV1 = mean(vect1)
mV2 = mean(vect2)
length = shape(vect1)[1]
# 协方差的分子部分
covV=(vect1-mV1)*(vect2-mV2).transpose()
# 方差的分子部分
dV1 = sum(power(vect1-mV1,2))
dV2 = sum(power(vect2-mV2,2))
# 相关系数就是两个向量的协方差的乘积/方差的乘积
corref = covV/sqrt(dV1*dV2)
print "corref:",corref
# 使用函数计算相关系数
corrcoefV = corrcoef(vect1,vect2)
print "corrcoef(vect1,vect2):",corrcoefV[0,1]

# 杰卡德距离
X = mat([[1, 1, 0],[1,-1, 0],[-1, 1, 0]])
Y = dist.pdist(X,'jaccard')
print "dist.jaccard:",Y

# 信息熵
classLabel = mat([0,1,1,1,0,1,1,1,0,1,0,0,1,0])
classlength = shape(classLabel)[1]
label0 = float(shape(nonzero((classLabel)==0)[0])[1])
label1 = float(shape(nonzero((classLabel)==1)[0])[1])
pl0 = label0/classlength
pl1 = label1/classlength
shannonEnt0 = -pl0*math.log(pl0,2)
shannonEnt1 = -pl1*math.log(pl1,2)
print "shannonEnt0:",shannonEnt0,"   shannonEnt1:",shannonEnt1
print