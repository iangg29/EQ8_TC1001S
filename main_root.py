import tkinter as tk


def launchApp():
    ventana = tk.Tk()  # Contenedor gráfico
    # Caracteriticas de la ventana:
    ventana.title("Filtro Tumblr")

    # Titulo y su formato
    titulo = tk.Label(ventana, font=("Arno Pro Smbd", 24), fg="white", text="Filtros Tumblr", bg="#556677", width=30,
                      height=2)
    titulo.grid(row=0, column=1, columnspan=3)

    l1 = tk.Label(ventana)
    l1.grid(row=1, column=1, columnspan=3)

    T = tk.Entry(ventana, font=("Arno Pro Smbd", 20))
    T.grid(row=2, column=1, columnspan=3)

    l2 = tk.Label(ventana)
    l2.grid(row=3, column=1, columnspan=3)

    boton1 = tk.Button(ventana, font=("Arial", 14), text="Box blur", command=lambda: filtroBox(T.get()))
    boton1.grid(row=4, column=1, columnspan=1)

    boton2 = tk.Button(ventana, font=("Arial", 14), text="Laplacian", command=lambda: filtroLaplacian(T.get()))
    boton2.grid(row=4, column=2, columnspan=1)

    boton3 = tk.Button(ventana, font=("Arial", 14), text="Repujado", command=lambda: filtroRep(T.get()))
    boton3.grid(row=4, column=3, columnspan=1)

    boton4 = tk.Button(ventana, font=("Arial", 14), text="Laplacian of Gaussian",
                       command=lambda: filtroLaplacianOfGaussian(T.get()))
    boton4.grid(row=4, column=4, columnspan=1)

    l3 = tk.Label(ventana)
    l3.grid(row=5, column=1, columnspan=3)

    # loop para mantener la ventana siempre visible
    ventana.mainloop()


if __name__ == '__main__':
    launchApp()
