# -*- coding: utf-8 -*-
# Filename : 06HandWriting.py

from numpy import *
import kNN2
import numpy as np 
import operator
from os import listdir

# 初始化分类标签
hwLabels = []
#加载训练集
#listdir('trainingDigits'): 列出 trainingDigits 里面的所有文件和目录，但不包括子目录中的内容。
trainingFileList = listdir('trainingDigits')           
# 返回目录中文件的数量
m = len(trainingFileList)
# 初始化训练集矩阵：每个数字为一个向量：1*1024
trainingMat = zeros((m,1024))

# 循环生成训练集矩阵
for i in range(m):
	  # 对训练集的文件名进行处理
    fileNameStr = trainingFileList[i]
    fileStr = fileNameStr.split('.')[0]     # 去除 .txt
    # 获得下划线分隔文件名的前半部分，并转换为整型
    # 该文件名就是分类标签
    classNumStr = int(fileStr.split('_')[0]) 
    # 附加为生成分类标签集
    hwLabels.append(classNumStr)  
    # 将训练集转换为向量形式,长度为1024    
    trainingMat[i,:] = kNN2.img2vector('trainingDigits/%s' % fileNameStr)
    	
# 列出 testDigits 里面的所有文件和目录，作为测试集。	
testFileList = listdir('testDigits')
errorCount = 0.0
# 测试集文件的数
mTest = len(testFileList)
# 循环每个测试集
for i in range(mTest):
	  # 对测试集的文件名进行处理 
    fileNameStr = testFileList[i]
    fileStr = fileNameStr.split('.')[0]     #去除后缀.txt
    # 文件名生成分类标签--用于测试
    classNumStr = int(fileStr.split('_')[0])
    # 将测试集转换为1024向量形式
    vectorUnderTest = kNN2.img2vector('testDigits/%s' % fileNameStr)
    # 将测试集应用相应的训练集进行kNN分类
    # vectorUnderTest 测试集元素
    # trainingMat 训练集
    # hwLabels, 训练集的分类标签集 
    # 3，k近邻
    classifierResult = kNN2.classify(vectorUnderTest, trainingMat, hwLabels, 3)
    print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
    if (classifierResult != classNumStr): errorCount += 1.0
print "\nthe total number of errors is: %d" % errorCount
print "\nthe total error rate is: %f" % (errorCount/float(mTest))