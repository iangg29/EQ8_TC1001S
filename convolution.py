import numpy as np
from add_padding import add_padding

def convolution(matriz, kernel, padding):
	"""
	Función para realizar la convolución de una matriz, con padding definido y stride de 1
	"""
	matriz = add_padding(matriz, padding)
	fil_m, col_m = matriz.shape
	fil_k, col_k = kernel.shape
	conv_final = np.zeros(((fil_m-fil_k)+1, (col_m-col_k)+1)) #Se declara matriz con dimensiones finales

	for i in range(conv_final.shape[0]):
		for j in range(conv_final.shape[1]):
			producto = np.multiply(matriz[i:i+fil_k, j:j+col_k], kernel)
			conv_final[i][j] = np.sum(producto)

	return(conv_final)