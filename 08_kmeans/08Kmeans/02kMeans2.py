# -*- coding: utf-8 -*-
# Filename : 02kMeans1.py

from numpy import *
import numpy as np 
import operator
import kMeans2
import matplotlib.pyplot as plt 

# ���ļ����������ݼ�    
dataSet = kMeans2.loadDataSet("testSet.txt")  
dataSet = mat(dataSet) # ת��Ϊ������ʽ

# ����ɢ��ͼͼ��
for mydata in dataSet:
	plt.scatter(mydata[0,0],mydata[0,1],c='blue',marker='o')

k = 4 # �ⲿָ��1,2,3... ͨ���۲����ݼ���4����������
m = shape(dataSet)[0] # ���ؾ��������

# ���㷨�������ݽṹ:���������ݼ���ͬ
# ��1�����ݼ���Ӧ�ľ�������,��2:���ݼ����������������ĵľ���
clusterAssment = mat(zeros((m,2)))

# �������һ�����ݼ��ľ�������:����Ϊ2*4�ľ���
# ȷ���þ�������λ��min(dataMat[:,j]),max(dataMat[:,j])֮��
centroids = kMeans2.randCent(dataSet, k) 

clusterChanged = True # ��ʼ����־λ,������ʼ
counter = []; #������ 

# ѭ������ֱ����ֹ����ΪFalse
# �㷨ֹͣ��������dataSet���������������ҵ�ĳ����������,�������ĵľ����С������k-1�����ĵľ���
while clusterChanged: 
    x1 = 0; x2 = 0;temp = [] #��������
    clusterChanged = False # �ָ���־λΪFalse
    
    #---- 1. ����clusterAssement�� ����DataSet���ݼ�,����DataSetÿ����centroids�������Сŷʽ���� ----#
    # �Լ���Ӧ��centroids�����������˽����ֵclusterAssement=[minIndex,minDist]
    for i in range(m): 
        minDist = inf # ��ʼ����Сŷʽ����Ϊ�����
        minIndex = -1 # ��ʼ����Сcentroids����ֵ-1
        
        # ����k����������
        # ����ÿ��dataSet��������k��centroids������֮���ŷʽ����
        # ѡ���������һ�е�centroids��������minIndex,��̾��븳��minDist
        for j in range(k):
        	# ����dataSet��i��, centroids��j(0~k-1)�е�ŷʽ����
        	# distJI = kMeans2.distEclud(centroids[j,:],dataSet[i,:]) 
        	distJI = sum(power(centroids[j,:] - dataSet[i,:], 2))
        		
        	#	��������distJIŷʽ����С����С����
        	if distJI < minDist:
        		minDist = distJI  # distJI->minDist
        		minIndex = j      # j->minIndex j��centroids�����±�    
        
        # ���clusterAssment��ǰ������ֵ��������С����ֵ
        if clusterAssment[i,0] != minIndex: 
        	clusterChanged = True # ���ñ�־λΪTrue����������
        	x1 +=1        # x1��¼�˲��ȵ�����
        else: x2 +=1	  # x2��¼����ȵ�����
        	
        # ��minIndex��minDist**2����clusterAssement��i�� 
        # ���������ݼ�i�ж�Ӧ�ľ�������ΪminIndex,��̾���ΪminDist 
        clusterAssment[i,:] = minIndex,minDist # **2 	 
    
    # �ۼƼ���
    temp.append(x1); temp.append(x2); counter.append(temp) #�������ۼ�   
     
    # ---- 2.����centroidsֵ: ѭ������Ϊcent(0~k-1)----#
    # 1.�þ�������cent�з�ΪclusterAssment������dataSet��������
    # ���Դ˴�dataSet����ȡ��Ӧ�������������µ�ptsInClust
    # ����ָ���ptsInClust���еľ�ֵ���Դ˸��¾�������centroids�ĸ���ֵ
    for cent in range(k):    	 
    	 #��clusterAssment�ĵ�һ����ɸѡ������centֵ�����±�
       #  clusterAssment[:,0].A==cent: �ж�clusterAssment��1��ÿ��Ԫ���Ƿ���cent���,�����ȷ���Ϊ1,����Ϊ0
       #  nonzero(clusterAssment[:,0].A==cent):����clusterAssment[:,0]����ֵ��������
       #  ��ά�����Ϊ����List:List1(���±�����);List2(���±�����)
       # print clusterAssment[:,0].A
       # print cent  
       dInx = nonzero(clusterAssment[:,0].A==cent)[0]
       # ��dataSet����ȡ���±�==dInx����һ�������ݼ�
       ptsInClust = dataSet[dInx]
       # ����ptsInClust���еľ�ֵ: mean(ptsInClust, axis=0):axis=0�ӵ�һ�п�ʼ
       # =[ptsInClust��1������ֵ֮��/ptsInClust����, ptsInClust��2������ֵ֮��/ptsInClust����...]
       centroids[cent,:] = mean(ptsInClust, axis=0) 

# ���ƾ�������
for cent in centroids:
	plt.scatter(cent[0,0],cent[0,1],s=60,c='red',marker='D')
plt.show() 

# ���ؼ�����ɵľ�������
print "centroids:"
print centroids
# ������ɵ�clusterAssment����Ӧ�ľ�������(��1),���������ĵľ���(��2),����dataSetһһ��Ӧ
print "clusterAssment:"
print clusterAssment
# ��������ͳ��clusterAssment ÿ��ѭ���� minIndex�ı仯
print "counter:"
print counter

