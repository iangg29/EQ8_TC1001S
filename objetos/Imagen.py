import cv2
import matplotlib.pyplot as plt
import numpy as np


class Imagen:
    def __init__(self, file):
        """
        Estructura principal de la imagen.
        :param file: Archivo de la imagen.
        """
        self.file = file
        self.original = cv2.imread(file)
        self.image = self.toGrayScale(self.original)

    def getFile(self):
        """
        :return: Archivo de la imagen
        """
        return self.file

    def getOriginal(self):
        """
        :return: Matriz de la imagen original. (Sin modificaciones)
        """
        return self.original

    def getImage(self):
        """
        :return: Matriz de la imagen. (En escala de grises)
        """
        return self.image

    def applyFilter(self, filter):
        """
        Aplicación de filtros a la imagen.
        Hace display a la imagen con el filtro aplicado.
        :param filter: Filtro a aplicar.
        """
        filtered = self.convolution(self.getImage(), filter.getKernel())

        plt.imshow(filtered, cmap='gray')
        plt.title(f"Imagen con filtro [{filter.getNombre()}]")
        plt.show()
        return filtered

    def convolution(self, matrix, kernel):
        """
        Ejecuta una evolución completa de la matriz y el kernel.
        * El padding de la matriz es dinámico en base al tamaño del kernel.
        :param matrix: Matriz principal a ejecutar la convolución.
        :param kernel: Kernel definido para la convolución.
        :return output: Convolución resultante en forma de matriz.
        """
        m_row, m_col = matrix.shape
        k_row, k_col = kernel.shape

        output = np.zeros(matrix.shape)

        padding_height = int((k_row - 1) / 2)
        padding_width = int((k_col - 1) / 2)

        padded_output = np.zeros((m_row + (2 * padding_height), m_col + (2 * padding_width)))

        padded_output[padding_height:padded_output.shape[0] - padding_height,
        padding_width:padded_output.shape[1] - padding_width] = matrix

        for i in range(m_row):
            for j in range(m_col):
                output[i, j] = np.sum(kernel * padded_output[i:i + k_row, j:j + k_col])
        return output

    def showOriginal(self):
        """
        Hace display a la imagen original sin modificaciones.
        :return: Matriz de la imagen original.
        """
        plt.imshow(self.original)
        plt.title(f"Imagen original [{self.getFile()}]")
        plt.show()
        return self.getOriginal()

    def toGrayScale(self, image):
        """
        Convierte una imagen de profundidad 3 a una bidimensional.
        :param image: Matriz de la imagen original.
        :return: Matriz resultante bidimensional.
        """
        if len(image.shape) == 3:
            return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image
