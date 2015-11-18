# -*- coding: utf-8 -*-
# Filename : 03bikMeans1.py

from numpy import *
import numpy as np 
import operator
import kMeans2
import matplotlib.pyplot as plt 

# 从文件构建的数据集    
dataSet = kMeans2.loadDataSet("testSet.txt")  
dataSet = mat(dataSet) # 转换为矩阵形式

# 绘制dataSet散点图形
for mydata in dataSet:
	plt.scatter(mydata[0,0],mydata[0,1],c='blue',marker='o')
 
k = 4 #分类数
m = shape(dataSet)[0] #dataSet的行数

# 聚类距离表:行数与数据集相同
# 列1：数据集对应的聚类中心,列2:数据集行向量到聚类中心的距离
clusterAssment = mat(zeros((m,2))) 

# 初始化第一个聚类中心: dataSet的每一列的均值
centroid0 = mean(dataSet, axis=0).tolist()[0]
# 把这个随机聚类中心加入聚类中心列表中
centList =[centroid0] 

# 初始化聚类距离表,距离方差: sum((centroid0-dataSet[j,:])^2)
# clusterAssment[j,1] = [0,方差]
# print centroid0

for j in range(m):
    clusterAssment[j,1] = sum(power(mat(centroid0)- dataSet[j,:], 2))	
# print clusterAssment
    	
# 判断 centList的长度是否小于k
while (len(centList) < k):
    lowestSSE = inf # 初始化最小误差平方和。核心参数，这个值越小就说明聚类的效果越好。
    # 遍历cenList的每个向量
    #----1. 使用clusterAssment计算lowestSSE，以此确定:bestCentToSplit、bestNewCents、bestClustAss----#
    for i in range(len(centList)):
        # 返回clusterAssment第1列==i所构成的行下标数组
        cAIndx = nonzero(clusterAssment[:,0].A==i)[0]
        # 用cAIndx过滤数据集,构成一个子集
        ptsInCurrCluster = dataSet[cAIndx,:]
        # 应用标准kMeans算法(k=2),将ptsInCurrCluster划分出两个聚类中心,以及对应的聚类距离表	
        centroidMat,splitClustAss = kMeans2.kMeans(ptsInCurrCluster, 2)
        # 计算splitClustAss的距离平方和
        sseSplit = sum(splitClustAss[:,1])
        # 返回clusterAssment第1列!=i所构成的行下标数组
        ucAIndx = nonzero(clusterAssment[:,0].A!=i)[0] 
        # 计算clusterAssment[clusterAssment第1列!=i的距离平方和
        sseNotSplit = sum(clusterAssment[ucAIndx,1])
        # 算法公式: lowestSSE = sseSplit + sseNotSplit
        if (sseSplit + sseNotSplit) < lowestSSE:
            bestCentToSplit = i                 # 确定聚类中心的最优分隔点 
            # print "i:",i   
            bestNewCents = centroidMat          # 用新的聚类中心更新最优聚类中心
            bestClustAss = splitClustAss.copy() # 深拷贝聚类距离表为最优聚类距离表
            # print "bestClustAss:",bestClustAss 
            lowestSSE = sseSplit + sseNotSplit  # 更新lowestSSE
            # print "lowestSSE:",lowestSSE        
    # 回到外循环
    #----2. 计算新的clusterAssment----#
    # 返回bestClustAss第1列==1所构成的行下标数组
    bIndx0 = nonzero(bestClustAss[:,0].A == 1)[0] # 分了两部分，第一部分
    # 为bestClustAss[bIndx0,0]赋值为聚类中心的索引
    bestClustAss[bIndx0,0] = len(centList) 
    # 返回bestClustAss第1列==0所构成的行下标数组
    bIndx1 = nonzero(bestClustAss[:,0].A == 0)[0] # 分了两部分，第二部分
    # 用最优分隔点的指定聚类中心索引 
    bestClustAss[bIndx1,0] = bestCentToSplit
    # print "bestClustAss:",bestClustAss
    #以上为计算bestClustAss
    # 返回clusterAssment第1列值==bestCentToSplit所构成的行下标数组
    cIndxb = nonzero(clusterAssment[:,0].A == bestCentToSplit)[0]
    # 更新clusterAssment对应最优分隔点下标的距离，使距离值等于最优聚类距离对应的值
    clusterAssment[cIndxb,:]= bestClustAss 
    #以上为计算clusterAssment
    
    #----3. 用最优分隔点来重构聚类中心----#
    # 覆盖: bestNewCents[0,:].tolist()[0]附加到原有聚类中心的bestCentToSplit位置
    # 增加: 聚类中心增加一个新的bestNewCents[1,:].tolist()[0]向量
    centList[bestCentToSplit] = bestNewCents[0,:].tolist()[0]
    centList.append(bestNewCents[1,:].tolist()[0]) 
    # print "centList:",centList	
    # 以上为计算centList

print "cenList:",mat(centList)
print "clusterAssment:", clusterAssment
# 绘制聚类中心图形
for cent in centList:
	plt.scatter(cent[0],cent[1],s=60,c='red',marker='D')
plt.show()


