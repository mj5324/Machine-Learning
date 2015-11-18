# -*- coding: utf-8  -*-
# Filename : kNN2.py

'''
Created on Sep 16, 2010
kNN: k Nearest Neighbors

Input:      inX: vector to compare to existing dataset (1xN)
            dataSet: size m data set of known vectors (NxM)
            labels: data set labels (1xM vector)
            k: number of neighbors to use for comparison (should be an odd number)
            
Output:     the most popular class label

@author: pbharrin
'''

from numpy import *
import operator
from os import listdir

# kNN分类器
# 测试集：inX
# 训练集：dataSet
# 类别标签：labels
# k:kNN中的k个邻居数
def classify(inX, dataSet, labels, k):
	  # 返回样本集的行数
    dataSetSize = dataSet.shape[0]
    
    # 计算测试集与训练集之间的距离：欧氏距离
    # 1.计算测试项与训练集各项的差
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    # 2.计算差的平方和
    sqDiffMat = diffMat**2
    # 3.按列求和
    sqDistances = sqDiffMat.sum(axis=1)
    # 4.生成均方差欧氏距离
    distances = sqDistances**0.5
    # 5.根据生成的欧氏距离大小排序,结果为索引号
    sortedDistIndicies = distances.argsort()     
   
    classCount={} 
    
    # 获取欧氏距离的前三项作为参考项          
    for i in range(k):  # i = 0~(k-1)  	  
    	  # 按序号顺序返回样本集对应的类别标签
        voteIlabel = labels[sortedDistIndicies[i]]
        print ("i=%s  sortedDistIndicies = %s  labels[%s]=%s" % (i,sortedDistIndicies[i],sortedDistIndicies[i],voteIlabel))        
        # 为字典classCount赋值,相同key，其value加1
        # key:voteIlabel  
        # value: 符合voteIlabel标签的训练集数 
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    print "classCount:",classCount
 
    # 对分类字典classCount按value重新排序
    # sorted(data.iteritems(), key=operator.itemgetter(1), reverse=True) 
    # 该句是按字典值排序的固定用法
    # classCount.iteritems()：字典迭代器函数
    # key：排序参数；operator.itemgetter(1)：多级排序
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    print "sortedClassCount:",sortedClassCount
    # 返回序最高的一项
    return sortedClassCount[0][0]

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels
    
# 数据文件转换为矩阵
def file2matrix(filename):
	  # 打开文件
    fr = open(filename)              
    # 获取数据集文件长度，值为1000           
    numberOfLines = len(fr.readlines())  
    # 初始化返回的数据矩阵，为矩阵行数为数据集文件长度1000，3列       
    returnMat = zeros((numberOfLines,3))   
    # 初始化类别标签向量       
    classLabelVector = []                        
    # 打开文件
    fr = open(filename)                         
    index = 0
    # 一行一行的读取数据文件
    for line in fr.readlines():  
    	  # 删除左右两侧空格               
        line = line.strip()            
        # 以TAB空格来分隔字符，每个值为矩阵的一个元素         
        listFromLine = line.split('\t')         
        # 把分隔好的矩阵某一行前三个元素赋值给returnMat中
        returnMat[index,:] = listFromLine[0:3]  
        # int(listFromLine[-1])：转至行向量的最后一个元素
        # 在类别向量中加入该类元素
        classLabelVector.append(int(listFromLine[-1])) 
        index += 1
        #返回数据矩阵
        #返回类别标签矩阵
    return returnMat,classLabelVector

# 数据集的归一化计算    
def autoNorm(dataSet):
	# 返回数据集的最小值矩阵，按列区分，返回每一列的最小值
    minVals = dataSet.min(0)
  # 返回数据集的最大值矩阵，按列区分，返回每一列的最大值  
    maxVals = dataSet.max(0)
  # 返回矩阵的范围值：最大值-最小值的范围
    ranges = maxVals - minVals
  # shape(dataSet):返回一个向量：矩阵的行与列的数量 
  # zeros(shape(dataSet)):初始化 normDataSet 为与dataSet相同的全零矩阵  
    normDataSet = zeros(shape(dataSet))
  # 初始化 normDataSet 为与dataSet相同的零矩阵  
    m = dataSet.shape[0]
  # 以最小值填充矩阵 tile(minVals, (m,1))
  # 原始数据集(dataSet)-最小值构成的矩阵：(x-MinValue)
    normDataSet = dataSet - tile(minVals, (m,1))    
  # 线性归一化核心公式：(x-MinValue)/(MaxValue-MinValue)
    normDataSet = normDataSet/tile(ranges, (m,1))   #element wise divide
  # 返回：
  # 归一化后的结果：normDataSet
  # 最小值：MinValue
  # 范围值：MaxValue-MinValue
    return normDataSet, ranges, minVals
   
def datingClassTest():
    hoRatio = 0.50      #hold out 10%
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')       #load data setfrom file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print "the total error rate is: %f" % (errorCount/float(numTestVecs))
    print errorCount

#图片转换向量的方法    
def img2vector(filename):
	  # 初始化长度为1024的向量
    returnVect = zeros((1,1024))
    # 打开文件
    fr = open(filename)
    # 每32个元素为1行，循环32次将矩阵累加为一个向量
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
            # print returnVect
    # 返回处理后的向量       
    return returnVect

# kNN分类的手写识别
def handwritingClassTest():
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
        classNumStr = int(fileStr.split('_')[0])  # 获得下划线分隔文件名的前半部分，并转换为整型
        hwLabels.append(classNumStr) # 通过文件名生成分类标签
        # 将训练集转换为向量形式   
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
   
    # 列出 testDigits 里面的所有文件和目录，作为测试集。    	
    testFileList = listdir('testDigits')   
    errorCount = 0.0
    mTest = len(testFileList) # 测试集文件的数量
    for i in range(mTest):
        fileNameStr = testFileList[i]   # 对测试集的文件名进行处理 
        fileStr = fileNameStr.split('.')[0]     # 去除 .txt
        classNumStr = int(fileStr.split('_')[0])  # 生成分类标签--用于测试
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)  # 将测试集转换为向量形式
        # 将测试集应用相应的训练集进行kNN分类
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
        if (classifierResult != classNumStr): errorCount += 1.0
    print "\nthe total number of errors is: %d" % errorCount
    print "\nthe total error rate is: %f" % (errorCount/float(mTest))