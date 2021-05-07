class Filtro:
    def __init__(self, nombre, kernel):
        """
        Estructura principal para filtros.
        :param nombre: Nombre del filtro.
        :param kernel: Kernel propio del filtro.
        """
        self.nombre = nombre
        self.kernel = kernel

    def getNombre(self):
        """
        :return: Nombre del filtro.
        """
        return self.nombre

    def getKernel(self):
        """
        :return: Kernel propio del filtro.
        """
        return self.kernel

    def setNombre(self, nombre):
        """
        Asigna nombre al filtro.
        :param nombre: Nombre del filtro.
        """
        self.nombre = nombre

    def setKernel(self, kernel):
        """
        Asigna kernel al filtro.
        :param kernel: Kernel del filtro.
        """
        self.kernel = kernel

    def __str__(self):
        """
        Display del objeto.
        :return: Nombre del filtro.
        """
        return self.nombre
