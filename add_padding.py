import numpy as np
"""
Función para agregar padding a una matriz

Se calcula una nueva matriz con  cierto grosor de 0s alrededor a partir de las dimensiones del kernel
"""
def add_padding(matriz, kernel):
    fil_m, col_m = matriz.shape
    fil_k, col_k = kernel.shape
    #Calculamos la cantidad de padding a partir de las dimensiones del kernel
    pad_height = int((fil_k - 1) / 2)
    pad_width = int((col_k - 1) / 2)
    #Creamos matriz con nuevas dimensiones (agregamos padding en los 4 lados)
    matriz_res = np.zeros(((fil_m + pad_height*2), (col_m + pad_weight*2)))
    matriz_res[pad_height:fil_m + pad_height, pad_width:col_m + pad_width] = matriz

    return(matriz_res)