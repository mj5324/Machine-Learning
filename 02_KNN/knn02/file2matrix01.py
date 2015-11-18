# -*- coding: utf-8 -*-
# Filename : 02file2matrix.py

from numpy import *
import operator
import numpy as np 
import matplotlib
import matplotlib.pyplot as plot

filename = 'datingTestSet2.txt'             # 导入的数据文件路径

fr = file(filename)                         # 打开文件对象

numberOfLines = len(fr.readlines())         # 获取数据集文件长度，值为1000

print numberOfLines                         # 输出文件的行数:1000

returnMat = zeros((numberOfLines,3))        # 初始化返回的数据矩阵，为矩阵行数为数据集文件长度1000，3列
# print returnMat  # 1000*3全零矩阵

classLabelVector = []                       # 初始化类别标签向量 

fr.close()                                  # 关闭文件对象

# 以上的步骤得到数据文件的行数，用以初始化数据矩阵的行数

fr = open(filename)                         # 再次打开文件对象

index = 0                                   # 初始化行索引值

for line in fr.readlines():                 # 按行读取数据文件
	  
    line = line.strip()                     # 删除左右两侧空格
    
    listFromLine = line.split('\t')         # 源文件每行是以TAB空格来分隔字符，每个值为矩阵的一个元素
    
    returnMat[index,:] = listFromLine[0:3]  # 把分隔好的矩阵前三个元素赋值给returnMat中 	
    	
    # print int(listFromLine[-1])           # 输出行向量的最后一个元素
    
    classLabelVector.append(int(listFromLine[-1])) # 在类别向量中加入该类元素
    
    index += 1

fr.close()                                  # 关闭文件对象

print returnMat                             # 输出转换后的数据矩阵

print classLabelVector                      # 输出类别标签