# -*- coding: utf-8 -*-
# Filename : matrix02.py

from numpy import *
import operator
import matplotlib.pyplot as plot

# 特殊的矩阵

# 全零矩阵：3行4列全0矩阵
m3_4 = [3,4]
myZero = zeros(m3_4)
print "myZero:",myZero
print 

# 全1矩阵
myOnes = ones(m3_4) 
print "myOnes:",myOnes
print 

# 随机矩阵:3行4列的0~1之间的随机数矩阵
myRand = random.rand(3,4)
print "myRand:",myRand
print 

# 均匀分布:用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。
myUniform = random.uniform(0,1)
print "myUniform:",myUniform
print 

# 单位阵
myEye = eye(3)
print "myEye:",myEye
print 

# 元素级运算：同行同列
myMat1 = ones(m3_4) 
myMat2 = random.rand(3,4)
M1 =  myMat1+myMat2 # 元素相加
M2 =  myMat1-myMat2 # 元素相减
print "M1:",M1
print "M2:",M2
print 

#所有元素的和
smmyMat1 = sum(myMat1)
print "smmyMat1:",smmyMat1
print 

# 矩阵各元素的积 matlab .*
A=[[1,2,3],[2,3,4],[4,5,6]];B=[[9,8,7],[6,5,4],[3,4,5]]
AB = multiply(A,B)
print "multiply(A,B):",AB
print 

# 矩阵各元素的n=2次幂
pwM2 = power(M2,2)
print "pwM2:",pwM2 # 或 M2**2
print 

# 矩阵各元素的开方
sqM2 = sqrt(pwM2)
print "sqM2:",sqM2 
print 

# 矩阵的乘法:将列表转换为mat，此时inner(A,B),dot(A,B) =A*B
A = [[1,2,3],[4,5,6],[7,8,9]];B = [[1],[4],[7]]
A=mat(A);B=mat(B) # 转换为二维矩阵
AB = dot(A,B) #计算A,B的点积
print "dot(A,B):",AB 
print "A*B=",A*B
