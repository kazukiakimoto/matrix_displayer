# coding: utf-8
# Released under the MIT licence https://opensource.org/licenses/mit-license.php
# Copyright © 2021 Kazuki Akimoto. All right reserved.

import numpy as np
from lib import mylib

if __name__ == '__main__':

	#初期化
	mat = np.zeros((2,2))

	#行列を設定
	print('行列の値を入力してください: ')
	#mat = np.array([[1,0], [0,2]])
	for row in range(2):
		for col in range(2):
			print('{}行{}列の値: '.format(row+1,col+1), end='')
			mat[row, col] = input()
	print('________________')

	#行列の情報を表示
	mylib.desplay_matrix(mat)
	mylib.transpose_matrix(mat)
	mylib.inverse_matrix(mat)
	mylib.determinant(mat)
	mylib.eigenvalue(mat)
