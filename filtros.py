import numpy as np

from objetos.Filtro import Filtro


class BoxBlur(Filtro):
    def __init__(self):
        super(BoxBlur, self).__init__("Box Blur", np.array([[1 / 9, 1 / 9, 1 / 9],
                                                            [1 / 9, 1 / 9, 1 / 9],
                                                            [1 / 9, 1 / 9, 1 / 9]]))


class LaplacianOp(Filtro):
    def __init__(self):
        super(LaplacianOp, self).__init__("Laplacian Op", np.array([[-1, -1, -1],
                                                                    [-1, 8, -1],
                                                                    [-1, -1, -1]]))


class Repujado(Filtro):
    def __init__(self):
        super(Repujado, self).__init__("Repujado", np.array([[-2, -1, 0],
                                                             [-1, 1, 1],
                                                             [0, 1, 2]]))


class LaplacianOfGaussian(Filtro):
    def __init__(self):
        super(LaplacianOfGaussian, self).__init__("Laplacian of Gaussian", np.array([[0, 0, -1, 0, 0],
                                                                                     [0, -1, -2, -1, 0],
                                                                                     [-1, -2, 16, -2, -1],
                                                                                     [0, -1, -2, -1, 0],
                                                                                     [0, 0, -1, 0, 0]]))


class EdgeDetection(Filtro):
    def __init__(self):
        super(EdgeDetection, self).__init__("Edge Detection", np.array([[-1, -1, -1],
                                                                        [-1, 8, -1],
                                                                        [-1, -1, -1]]))
