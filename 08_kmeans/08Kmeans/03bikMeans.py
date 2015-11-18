# -*- coding: utf-8 -*-
# Filename : 03bikMeans1.py

from numpy import *
import numpy as np 
import operator
import kMeans2
import matplotlib.pyplot as plt 

# ���ļ����������ݼ�    
dataSet = kMeans2.loadDataSet("testSet.txt")  
dataSet = mat(dataSet) # ת��Ϊ������ʽ

# ����dataSetɢ��ͼ��
for mydata in dataSet:
	plt.scatter(mydata[0,0],mydata[0,1],c='blue',marker='o')
 
k = 4 #������
m = shape(dataSet)[0] #dataSet������

# ��������:���������ݼ���ͬ
# ��1�����ݼ���Ӧ�ľ�������,��2:���ݼ����������������ĵľ���
clusterAssment = mat(zeros((m,2))) 

# ��ʼ����һ����������: dataSet��ÿһ�еľ�ֵ
centroid0 = mean(dataSet, axis=0).tolist()[0]
# ���������������ļ�����������б���
centList =[centroid0] 

# ��ʼ����������,���뷽��: sum((centroid0-dataSet[j,:])^2)
# clusterAssment[j,1] = [0,����]
# print centroid0

for j in range(m):
    clusterAssment[j,1] = sum(power(mat(centroid0)- dataSet[j,:], 2))	
# print clusterAssment
    	
# �ж� centList�ĳ����Ƿ�С��k
while (len(centList) < k):
    lowestSSE = inf # ��ʼ����С���ƽ���͡����Ĳ��������ֵԽС��˵�������Ч��Խ�á�
    # ����cenList��ÿ������
    #----1. ʹ��clusterAssment����lowestSSE���Դ�ȷ��:bestCentToSplit��bestNewCents��bestClustAss----#
    for i in range(len(centList)):
        # ����clusterAssment��1��==i�����ɵ����±�����
        cAIndx = nonzero(clusterAssment[:,0].A==i)[0]
        # ��cAIndx�������ݼ�,����һ���Ӽ�
        ptsInCurrCluster = dataSet[cAIndx,:]
        # Ӧ�ñ�׼kMeans�㷨(k=2),��ptsInCurrCluster���ֳ�������������,�Լ���Ӧ�ľ�������	
        centroidMat,splitClustAss = kMeans2.kMeans(ptsInCurrCluster, 2)
        # ����splitClustAss�ľ���ƽ����
        sseSplit = sum(splitClustAss[:,1])
        # ����clusterAssment��1��!=i�����ɵ����±�����
        ucAIndx = nonzero(clusterAssment[:,0].A!=i)[0] 
        # ����clusterAssment[clusterAssment��1��!=i�ľ���ƽ����
        sseNotSplit = sum(clusterAssment[ucAIndx,1])
        # �㷨��ʽ: lowestSSE = sseSplit + sseNotSplit
        if (sseSplit + sseNotSplit) < lowestSSE:
            bestCentToSplit = i                 # ȷ���������ĵ����ŷָ��� 
            # print "i:",i   
            bestNewCents = centroidMat          # ���µľ������ĸ������ž�������
            bestClustAss = splitClustAss.copy() # �����������Ϊ���ž�������
            # print "bestClustAss:",bestClustAss 
            lowestSSE = sseSplit + sseNotSplit  # ����lowestSSE
            # print "lowestSSE:",lowestSSE        
    # �ص���ѭ��
    #----2. �����µ�clusterAssment----#
    # ����bestClustAss��1��==1�����ɵ����±�����
    bIndx0 = nonzero(bestClustAss[:,0].A == 1)[0] # ���������֣���һ����
    # ΪbestClustAss[bIndx0,0]��ֵΪ�������ĵ�����
    bestClustAss[bIndx0,0] = len(centList) 
    # ����bestClustAss��1��==0�����ɵ����±�����
    bIndx1 = nonzero(bestClustAss[:,0].A == 0)[0] # ���������֣��ڶ�����
    # �����ŷָ����ָ�������������� 
    bestClustAss[bIndx1,0] = bestCentToSplit
    # print "bestClustAss:",bestClustAss
    #����Ϊ����bestClustAss
    # ����clusterAssment��1��ֵ==bestCentToSplit�����ɵ����±�����
    cIndxb = nonzero(clusterAssment[:,0].A == bestCentToSplit)[0]
    # ����clusterAssment��Ӧ���ŷָ����±�ľ��룬ʹ����ֵ�������ž�������Ӧ��ֵ
    clusterAssment[cIndxb,:]= bestClustAss 
    #����Ϊ����clusterAssment
    
    #----3. �����ŷָ������ع���������----#
    # ����: bestNewCents[0,:].tolist()[0]���ӵ�ԭ�о������ĵ�bestCentToSplitλ��
    # ����: ������������һ���µ�bestNewCents[1,:].tolist()[0]����
    centList[bestCentToSplit] = bestNewCents[0,:].tolist()[0]
    centList.append(bestNewCents[1,:].tolist()[0]) 
    # print "centList:",centList	
    # ����Ϊ����centList

print "cenList:",mat(centList)
print "clusterAssment:", clusterAssment
# ���ƾ�������ͼ��
for cent in centList:
	plt.scatter(cent[0],cent[1],s=60,c='red',marker='D')
plt.show()


