# -*- coding: utf-8 -*-
# Filename : matrix_defs.py

from numpy import *
import numpy.linalg

# 矩阵的转置
def transposeMat(matA):
	m,n = shape(matA)
	rtnMat = zeros((n,m))
	for i in range(n):
		for j in range(m):
			rtnMat[i,j] = matA[j,i]
	return rtnMat
	

# 矩阵的行列式
def detMat(matA): 
	s = 0;
	m,n=shape(matA)
	if m !=n : 
		print "m,n not equal"
		return 
	if 0 == n: return 0;
	if 1 == n: return  matA[0,0]; 	#/*阶为1，按照定义计算*/
	if 2 == n: return  matA[0,0]*matA[1,1]-matA[0,1]*matA[1,0]; 		
	
	lenth = n - 1;#子行列式的阶
	#/*按照定义，初始化一个子行列式数组的空间*/
	p = zeros((lenth,lenth))
	for k in range(n):
		for i in range(lenth):
			for j in range(lenth):
				if (i < k) :
					p[i,j] = matA[i,(j + 1)]; # 初始化子行列式的值
				if (i >= k):
					p[i,j] = matA[(i + 1),(j + 1)];
		s += power(-1, k) * matA[k,0] * detMat(p);# 递归计算
	return s;

# 矩阵的逆        
def inverse(Amat):	
	m,T = shape(Amat)
	if m != T : 
		print "不是方阵,无逆"
		return	
	if detMat(Amat)==0 :
		print "行列式为0,无逆"
		return
	matA = mat(zeros((T,2*T)))
	matA[:,0:T] = Amat[:,0:T]
	# 构造中间矩阵	
	invA = matA.copy()
	invA[:,T:2*T] = eye(T)[:,0:T] 	
	for i in range(T):
		for k in range(T):
			if (k != i):
				t = invA[k,i] / invA[i,i];
				for j in range(2*T):
					x = invA[i,j] * t;
					invA[k,j] = invA[k,j] - x;
	i = 0
	for inv in invA:
		invA[i,:] = inv/invA[i,i]
		i += 1				
	matA = invA[:,T:2*T]
	return matA
	  
# 矩阵乘法
def multiMat(matA,matB):
	ma,na = shape(matA)
	mb,nb = shape(matB)
	dotmat = mat(zeros((ma,nb)))
	# 判断是否能相乘
	if na != mb :
		print ("%s 不等于 %s,两矩阵不能相乘!"%(na,mb))
		return		
	for i in range(ma) :
		for j in range(nb) :
			msum = 0
			for k in range(mb) :
				msum += matA[i,k]*matB[k,j]
				dotmat[i,j] = msum
	return dotmat		 
	
# 计算向量的点积
def dotVect(matA,matB):
	vectA = matA.tolist()[0]
	vectB = matB.tolist()[0]
	vSum = 0 		
	dim = len(vectA) 
	if dim != len(vectB):
		print ("向量不同维, 或不是向量，不能相乘!")
		return	
	for i in range(dim):
		vSum += vectA[i]*vectB[i]
	return vSum
	
def vectMulti(matA,matB):
	ma,na = shape(matA)
	mb,nb = shape(matB) 	
	dotvect = mat(zeros((ma,nb)))	
	if na != 1 and mb != 1 :
		print ("%s,%s不等于1, 两向量不能相乘!"%(na,mb))
		return	
	j = 0
	for i in range(ma):
		for j in range(nb):
			dotvect[i,j] = matA[i,0]*matB[0,j]
	return dotvect
	
def smartMulti(matA,matB):
	ma,na = shape(matA)
	mb,nb = shape(matB)
	dotmat = mat(zeros((ma,nb)))
	# 判断是否能相乘
	if na != mb :
		print ("%s 不等于 %s,两矩阵不能相乘!"%(na,mb))
		return		
	for i in range(na) :
		dotmat += vectMulti(matA[:,i],matB[i,:])		
	return dotmat	
						
# 矩阵求秩
def rank(matA) :
	m,n = shape(matA);
	nn=m;
	a = matA
	if (m>=n): nn=n;
	k=0;
	for l in range(0,nn-1): 
		q = 0.0;
		for i in range(1,m-1): 
			for j in range(1,n-1): 
				d = abs(a[i,j]);
				if (d > q):
					q = d;
					si = i;
					js = j;
		if (q + 1.0 == 1.0): break;
		k = k + 1;
		if (si != l): 
			for j in range(l,n-1): 
				d = a[l,j];
				a[l,j] = a[si,j];
				a[si,j] = d;
				
		if (js != l) :
			for i in range(m-1): 
				d = a[i,js];
				a[i,js] = a[i,l];
				a[i,l] = d;

		for  i in range(l+1,n-1): 
			d = a[i,l] / a[l,l];
			for i in range(l+1,n-1): 
				a[i,j] = a[i,j] - d * a[l,j];
	return k

# 行最简形--阶梯矩阵
def rref(matA):
	lead = 0;
	rowCount, columnCount = shape(matA)
	for r in range(rowCount): 
		if (columnCount <= lead):
			break;
		i = r;
		while (matA[i, lead] == 0):
			i +=1 ;
			if (i == rowCount):
				i = r;
				lead +=1 ;
				if (columnCount == lead):
					lead -= 1
					break;
		for j in range(columnCount):
			temp = matA[r, j]
			matA[r, j] = matA[i, j]
			matA[i, j] = temp
        
		div = matA[r, lead];
		if div ==0 : div =1.0e-10
		for j in range(0,columnCount): 
			matA[r, j] /= div;                
		for j in range(rowCount): 
			if (j != r):
				sub = matA[j, lead];
				for k in range(columnCount): 
					matA[j, k] -= (sub * matA[r, k]);
		lead +=1;
	return matA
	
# 行最简形-另一个算法
def ToReducedRowEchelonForm(M):
  if not M: return
  lead = 0
  rowCount = len(M)
  columnCount = len(M[0])
  for r in range(rowCount):
      if lead >= columnCount:
          return
      i = r
      while M[i][lead] == 0:
          i += 1
          if i == rowCount:
              i = r
              lead += 1
              if columnCount == lead:
                  return
      M[i],M[r] = M[r],M[i]
      lv = M[r][lead]
      M[r] = [ mrx / lv for mrx in M[r]]
      for i in range(rowCount):
          if i != r:
              lv = M[i][lead]
              M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
      lead += 1
  return M    

# 施密特正交法:gram_schmidt(A)
def gram_schmidt(A):
	Num=0;#迭代步数
	Ahang,Alie = shape(A)  #矩阵的行和列
	dim = max(Ahang,Alie)
	v = mat(zeros((Ahang,Alie)));
	h = mat(zeros((Ahang,Alie)));
	v[:,0] = A[:,0] / linalg.norm(A[:,0])
	for j in range(1,Alie):
		for i in range(0,j):
			vsum = mat(zeros((Ahang,Alie))) #临时变量 存储后面的求和	
			for k in range(0,j):
				h[k,j] = A[:,j].transpose()*v[:,k]
				vsum[:,0] = vsum[:,0]+float(h[k,j])*v[:,k]
				Num = Num+1
			v[:,j] = A[:,j] - vsum[:,0]
			v[:,j] = v[:,j] / linalg.norm(v[:,j]);
	# print "Num:",Num			
	return v

 

	