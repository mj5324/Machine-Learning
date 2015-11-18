# -*- coding: utf-8 -*-
# Filename : 02kMeans1.py

from numpy import *
import numpy as np 
import operator
import kMeans2
import matplotlib.pyplot as plt 

# 从文件构建的数据集    
dataSet = kMeans2.loadDataSet("testSet.txt")  
dataSet = mat(dataSet) # 转换为矩阵形式

# 绘制散点图图形
for mydata in dataSet:
	plt.scatter(mydata[0,0],mydata[0,1],c='blue',marker='o')

k = 4 # 外部指定1,2,3... 通过观察数据集有4个聚类中心
m = shape(dataSet)[0] # 返回矩阵的行数

# 本算法核心数据结构:行数与数据集相同
# 列1：数据集对应的聚类中心,列2:数据集行向量到聚类中心的距离
clusterAssment = mat(zeros((m,2)))

# 随机生成一个数据集的聚类中心:本例为2*4的矩阵
# 确保该聚类中心位于min(dataMat[:,j]),max(dataMat[:,j])之间
centroids = kMeans2.randCent(dataSet, k) 

clusterChanged = True # 初始化标志位,迭代开始
counter = []; #计数器 

# 循环迭代直至终止条件为False
# 算法停止的条件：dataSet的所有向量都能找到某个聚类中心,到此中心的距离均小于其他k-1个中心的距离
while clusterChanged: 
    x1 = 0; x2 = 0;temp = [] #计数参数
    clusterChanged = False # 恢复标志位为False
    
    #---- 1. 构建clusterAssement： 遍历DataSet数据集,计算DataSet每行与centroids矩阵的最小欧式距离 ----#
    # 以及对应的centroids行索引，将此结果赋值clusterAssement=[minIndex,minDist]
    for i in range(m): 
        minDist = inf # 初始化最小欧式距离为无穷大
        minIndex = -1 # 初始化最小centroids索引值-1
        
        # 遍历k个聚类中心
        # 计算每个dataSet行向量与k个centroids行向量之间的欧式距离
        # 选出距离最短一行的centroids索引赋给minIndex,最短距离赋给minDist
        for j in range(k):
        	# 计算dataSet第i行, centroids第j(0~k-1)行的欧式距离
        	# distJI = kMeans2.distEclud(centroids[j,:],dataSet[i,:]) 
        	distJI = sum(power(centroids[j,:] - dataSet[i,:], 2))
        		
        	#	如果计算的distJI欧式距离小于最小距离
        	if distJI < minDist:
        		minDist = distJI  # distJI->minDist
        		minIndex = j      # j->minIndex j是centroids的行下标    
        
        # 如果clusterAssment当前的索引值不等于最小索引值
        if clusterAssment[i,0] != minIndex: 
        	clusterChanged = True # 重置标志位为True，继续迭代
        	x1 +=1        # x1记录了不等的数量
        else: x2 +=1	  # x2记录了相等的数量
        	
        # 将minIndex和minDist**2赋予clusterAssement第i行 
        # 含义是数据集i行对应的聚类中心为minIndex,最短距离为minDist 
        clusterAssment[i,:] = minIndex,minDist # **2 	 
    
    # 累计计数
    temp.append(x1); temp.append(x2); counter.append(temp) #计数器累计   
     
    # ---- 2.更新centroids值: 循环变量为cent(0~k-1)----#
    # 1.用聚类中心cent切分为clusterAssment，返回dataSet的行索引
    # 并以此从dataSet中提取对应的行向量构成新的ptsInClust
    # 计算分隔后ptsInClust各列的均值，以此更新聚类中心centroids的各项值
    for cent in range(k):    	 
    	 #从clusterAssment的第一列中筛选出等于cent值的行下标
       #  clusterAssment[:,0].A==cent: 判断clusterAssment第1列每个元素是否与cent相等,如果相等返回为1,否则为0
       #  nonzero(clusterAssment[:,0].A==cent):返回clusterAssment[:,0]非零值的索引，
       #  二维的情况为两个List:List1(行下标数组);List2(列下标数组)
       # print clusterAssment[:,0].A
       # print cent  
       dInx = nonzero(clusterAssment[:,0].A==cent)[0]
       # 从dataSet中提取行下标==dInx构成一个新数据集
       ptsInClust = dataSet[dInx]
       # 计算ptsInClust各列的均值: mean(ptsInClust, axis=0):axis=0从第一列开始
       # =[ptsInClust第1列所有值之和/ptsInClust行数, ptsInClust第2列所有值之和/ptsInClust行数...]
       centroids[cent,:] = mean(ptsInClust, axis=0) 

# 绘制聚类中心
for cent in centroids:
	plt.scatter(cent[0,0],cent[0,1],s=60,c='red',marker='D')
plt.show() 

# 返回计算完成的聚类中心
print "centroids:"
print centroids
# 输出生成的clusterAssment：对应的聚类中心(列1),到聚类中心的距离(列2),行与dataSet一一对应
print "clusterAssment:"
print clusterAssment
# 计数器：统计clusterAssment 每次循环后 minIndex的变化
print "counter:"
print counter

