from tkinter import *
from tkinter import messagebox

from objetos.Imagen import Imagen
from filtros import *


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
        box = Button(main, font=("Arial", 14), text="Box blur", command=lambda: image.applyFilter(BoxBlur()),
                     justify=CENTER, padx=30, pady=4)
        box.grid(row=1, column=1)
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
