from tkinter import *
from tkinter import messagebox

from filtros import *
from objetos.Imagen import Imagen


class GUI:
    def __init__(self, name):
        self.name = name
        self.tk = Tk()

    def getTK(self):
        return self.tk

    def getName(self):
        return self.name

    def processImg(self, input):
        if not input:
            messagebox.showwarning(message="Por favor introduce el nombre de la imagen!", title="Error!")
        image = Imagen(input)
        filters = Toplevel(self.getTK())
        filters.title("Selecciona el filtro")
        top = Frame(filters)
        top.pack(side=TOP)
        titulo = Label(top, font=("Arno Pro Smbd", 16), fg="white", bg="#556677", text="Filtros disponibles",
                       height=2, width=35)
        titulo.pack(side=LEFT)
        main = Frame(filters, height=40)
        main.pack(pady=30)
        original = Button(main, font=("Arial", 14), text="Original", command=lambda: image.showOriginal(),
                          justify=CENTER, padx=30, pady=4)
        original.grid(row=1, column=1, pady=10)
        box = Button(main, font=("Arial", 14), text="Box blur", command=lambda: image.applyFilter(BoxBlur()),
                     justify=CENTER, padx=30, pady=4)
        box.grid(row=2, column=1, pady=10)
        laplacianop = Button(main, font=("Arial", 14), text="Laplacian Op",
                             command=lambda: image.applyFilter(LaplacianOp()),
                             justify=CENTER, padx=20, pady=4)
        laplacianop.grid(row=3, column=1, pady=10)
        repujado = Button(main, font=("Arial", 14), text="Repujado", command=lambda: image.applyFilter(Repujado()),
                          justify=CENTER, padx=30, pady=4)
        repujado.grid(row=4, column=1, pady=10)
        laplacianogaussian = Button(main, font=("Arial", 14), text="Laplacian Of Gaussian",
                                    command=lambda: image.applyFilter(LaplacianOfGaussian()),
                                    justify=CENTER, padx=2, pady=4)
        laplacianogaussian.grid(row=5, column=1, pady=10)
        edge = Button(main, font=("Arial", 14), text="Edge detection",
                      command=lambda: image.applyFilter(EdgeDetection()),
                      justify=CENTER, padx=20, pady=4)
        edge.grid(row=6, column=1, pady=10)
        bottom = Frame(filters)
        bottom.pack(side=BOTTOM)
        exitButton = Button(bottom, text="Regresar", fg="#556677", command=lambda: filters.destroy(), justify=CENTER,
                            padx=30, pady=4)
        exitButton.pack(side=RIGHT, pady=20, padx=20)
        filters.mainloop()

    def start(self):
        self.getTK().title(self.getName())
        top = Frame(self.getTK())
        top.pack(side=TOP)
        titulo = Label(top, font=("Arno Pro Smbd", 24), fg="white", bg="#556677", text="Selecciona la imagen",
                       height=2, width=35)
        titulo.pack(side=LEFT)
        main = Frame(self.getTK(), height=30)
        main.pack(pady=30)
        placeHolder = Label(main, font=("Arno Pro Smbd", 20), text="Nombre del archivo:")
        placeHolder.pack(side=LEFT)
        imagen = Entry(main, font=("Arno Pro Smbd", 20))
        imagen.pack(side=RIGHT)
        bottom = Frame(self.getTK())
        bottom.pack(side=BOTTOM)
        exitButton = Button(bottom, text="Salir", fg="red", command=lambda: self.stop(), justify=CENTER,
                            padx=30, pady=4)
        exitButton.pack(side=RIGHT, pady=20, padx=20)
        process = Button(bottom, text="Procesar", fg="#556677", command=lambda: self.processImg(imagen.get()),
                         justify=CENTER,
                         padx=30, pady=4)
        process.pack(side=LEFT, pady=20, padx=20)
        self.getTK().mainloop()

    def stop(self):
        self.getTK().destroy()
