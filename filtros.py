import numpy as np
import matplotlib.pyplot as plt
import cv2
from convolution import convolution

def box_blur(imagen):
	"""
	Función para aplicar el filtro de box blur a una imagen y desplegarla

	Se utiliza la función de convolución para aplicar el filtro y la librería matplotlib para mostrar la imagen
	"""
	
	kernel = np.array([[1/9, 1/9, 1/9],
					[1/9, 1/9, 1/9],
					[1/9, 1/9, 1/9]])
		
	if len(imagen.shape) == 3: #Se cambia la imagen a escala de grises si es necesario
		imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

	imagen_conv = convolution(imagen, kernel)

	plt.imshow(imagen_conv, cmap='gray')
	plt.title("Imagen con filtro aplicado")
	plt.show()

def laplacian_op(imagen):
	"""
	Función para aplicar el operador laplaciano a una imagen y desplegarla

	Se utiliza la función de convolución para aplicar el filtro y la librería matplotlib para mostrar la imagen
	"""
	kernel = np.array([[-1, -1, -1],
					  [-1, 8, -1],
					  [-1, -1, -1]])
		
	if len(imagen.shape) == 3: #Se cambia la imagen a escala de grises si es necesario
		imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

	imagen_conv = convolution(imagen, kernel)

	plt.imshow(imagen_conv, cmap='gray')
	plt.title("Imagen con filtro aplicado")
	plt.show()
	

