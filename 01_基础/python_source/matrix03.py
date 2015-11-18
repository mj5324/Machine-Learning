# -*- coding: utf-8 -*-
# Filename : matrix04.py

from numpy import *
import numpy.linalg
import operator
import matrix_defs
import matplotlib.pyplot as plot

# 线性代数:

# 二、矩阵: 

# n阶行列式的运算
A = [[1,2,4,5,7,],[9,12,11,8,2,],[6,4,3,2,1,],[9,1,3,4,5],[0,2,3,4,1]]
detA =linalg.det(A);
print "linalg.det(A):",detA
print
# 矩阵的乘法:将列表转换为mat，此时inner(A,B),dot(A,B) =A*B
# 矩阵乘法的条件:第一个矩阵m*x的列数与第二个矩阵x*n的行数一样,相乘之后的结果为m*n
A = [[1,2,3],[4,5,6],[7,8,9]];B = [[1],[4],[7]]
A = mat(A);B = mat(B)
AB = dot(A,B)
print "dot(A,B):",AB # A*B
print
# 矩阵的转置
A = mat([[1,2,3],[4,5,6],[7,8,9]])
AT = A.T
print "A.T",AT
print
# 矩阵的逆:inv()
A = [[8,1,6],[3,5,7],[4,9,2]]
invA = linalg.inv(A)
print "linalg.inv(A):",invA
print
# 产生对称矩阵
A = mat([[8,1,6],[3,5,7]])
AT = A.T
SYMA = A*AT
print "矩阵的对称:",SYMA 
print "对称矩阵的逆矩阵:",linalg.inv(SYMA)
print

# 矩阵的秩:自定义函数
# A = [[2,4,1,3],[-1,-2,1,0],[0,0,2,2]]
A = [[1,2,2,2],[2,4,6,8],[3,6,8,10]]
# 矩阵求秩
rank = mat(A).ndim 
print "mat(A).ndim:",rank
print
# 自定义化行最简形
print matrix_defs.rref(mat(A))
print
# 齐次和非齐次线性方程组的解1:方阵且可逆
A = [[8,1,6],[3,5,7],[4,9,2]] #x1,x2,x3
b = [1,0,0] # 解矩阵
S = linalg.solve(A,transpose(b))
print "linalg.solve(A,b):",S
print
# 使用逆矩阵求方程组的解
S = (matrix_defs.inverse(mat(A))*mat(b).transpose())
print "(matrix_defs.inverse(mat(A))*mat(b).transpose()):",S
print
