# coding: utf-8
import numpy as np

# もとの行列を表示
def desplay_matrix(mat):
	print('行列は')
	print(mat)
	print('________________')

# 転置行列
def transpose_matrix(mat):
	print('転置行列は')
	print(mat.T)
	print('________________')

# 逆行列
def inverse_matrix(mat):
	print('逆行列は')
	try:
		print(np.linalg.inv(mat))
	except np.linalg.LinAlgError:
		print('エラー：この行列には逆行列が存在しません')
	print('________________')

#行列式
def determinant(mat):
	print('行列式は')
	print(np.linalg.det(mat))
	print('________________')

#固有値、固有ベクトル
def eigenvalue(mat):
	print('固有値・固有ベクトルは')
	w, v = np.linalg.eig(mat)
	print('固有値 :{}, 固有ベクトル:{}'.format(w[0],v[0]))
	print('固有値 :{}, 固有ベクトル:{}'.format(w[1],v[1]))
	print('________________')
