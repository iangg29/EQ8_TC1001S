#José Ángel Rico Mendieta

import tkinter as tk #Libreria gráfica
import cv2
from filtros import *
import matplotlib.pyplot as plt

def original(file):
    img = cv2.imread(file)
    plt.imshow(img)
    plt.title("Imagen original")
    plt.show()
    return img

def filtroBox(file):
    box_blur(original(file))  

def filtroLaplacian(file):
    laplacian_op(original(file))   
  
def main(): #Metodo principal   
    ventana=tk.Tk() #Contenedor gráfico
    #Caracteriticas de la ventana:
    ventana.title("Filtro Tumblr")
    
    #Titulo y su formato
    titulo = tk.Label(ventana,font=("Arno Pro Smbd",24),fg="white",text= "Filtros Tumblr", bg="#556677",width=20, height=2)
    titulo.grid(row=0, column=1, columnspan=2)
    
    l1 = tk.Label(ventana)
    l1.grid(row=1, column=1, columnspan=2)
    
    T = tk.Entry(ventana, font=("Arno Pro Smbd",20))
    T.grid(row=2,column=1, columnspan=2)

    l2 = tk.Label(ventana)
    l2.grid(row=3, column=1, columnspan=2)

    boton1 = tk.Button(ventana,font=("Arial",14), text="Box blur", command = lambda: filtroBox(T.get()))
    boton1.grid(row=4,column=1,columnspan=1)

    boton2 = tk.Button(ventana,font=("Arial",14), text="Laplacian", command = lambda: filtroLaplacian(T.get()))
    boton2.grid(row=4,column=2,columnspan=1)

    l3 = tk.Label(ventana)
    l3.grid(row=5, column=1,columnspan=2)

    #loop para mantener la ventana siempre visible
    ventana.mainloop()

#Se ejecuta la funcion principal
main()