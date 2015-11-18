# -*- coding: utf-8 -*-
# Filename : testSvd01.py

from numpy import *
import numpy as np 
import operator
import svdRec2
import matplotlib.pyplot as plt 

eps = 1.0e-6
# 加载修正后数据
Data = svdRec2.loadReData()
dataMat = mat(Data)

# 图像压缩
svdRec2.imgCompress()

