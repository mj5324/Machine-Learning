# -*- coding: utf-8 -*-
# Filename : matrix01.py

from numpy import *
import operator
import matplotlib.pyplot as plot

# 矩阵的操作:

# 使用list初始化矩阵
myArr = []
arr1 = [ 3.542485,1.977398,0 ]
arr2 = [ 3.018896,2.556416,1 ]
arr3 = [ 1,2,3 ]
arr4 = [ 7.551510,-1.580030,1]
# 使用append构成二维数组矩阵
myArr.append(arr1)
myArr.append(arr2)
myArr.append(arr4)
# 初始化 numpy 矩阵
mymat=mat(myArr)
print "mymat:",mymat
print

# 矩阵转置: numpy的matrix函数
mymatT = transpose(mymat)
print "mymatT:",mymatT
print

# 矩阵增加列: matrix->list->matrix
# 1.转换：tolist()
# 2.附加: append()
# 3.转置: transpose()
myArrT = mymatT.tolist()
myArrT.append(arr3)
mymat = transpose(myArrT)
print "mymat:",mymat
print

# 矩阵删除行:list 层
myArr1 = mymat.tolist()
myArr1.pop(1) # del myArr1[1]
mymat2 = mat(myArr1)
print "mymat:",mymat2
print

# 矩阵删除列:list 层
mymatT = transpose(mymat)
myArr2 = mymatT.tolist()
myArr2.pop(1)
mymat = transpose(myArr2)
print "mymat:",mymat
print

# 获取矩阵的行列
# shape(): 获取行、列--list,matrix 层 
[m,n]=shape(mymat)
print m,n
print

# 简单遍历矩阵:第2列
print "mymat[:,1]",mymat[:,1]
	
# 简单遍历矩阵:第2行
print "mymat[1,:]",mymat[1,:]	
print

# 循环遍历1-行遍历:list层
i = 0
for elem in mymat:
 	print "mymat[%s,:]=%s,%s,%s"%(i,elem[0],elem[1],elem[2])
 	i = i+1;
print

# 循环遍历2-列遍历:n为矩阵的列数
for col in range(n):
 	print "mymat[:,%s]=%s,%s,%s"%(col,mymat[0,col],mymat[1,col],mymat[2,col])
print

# 矩阵的分割
col1 = mymat[:,1]	 	 # 按列分割
raw1 = mymat[1,:]    # 按行分割
print "col1:",col1  
print "raw1:",raw1
print
# 矩阵的复制:深层复制 --matrix层
mymatcp = mymat.copy() # 转换为numpy矩阵形式,进行深层复制
print "mymatcp:",mymatcp
print
# 矩阵的排序和逆序--list层
matarr = mymatcp.tolist()[1]
matarr.sort()
print matarr
print
matarr.reverse()
print matarr
print
# 检验数据类型
print "type(matarr):",type(matarr)  # list
print "type(mymat):",type(mymat)   # matrix
print
# 判断列表相等
A= [1,2,3];B= [1,2,3]
print "A == B:", A == B
print "A is B:", A is B
print
# 判断矩阵的大小
A = mat([1,2,3]); B = mat([4,5,6])
print "A<B:",A<B
print
# 返回矩阵最大的元素
print "max:",A.max(),"  min:",B.min()
print