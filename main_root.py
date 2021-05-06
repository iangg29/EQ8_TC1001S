#José Ángel Rico Mendieta

import tkinter as tk #Libreria gráfica
import cv2
from filtros import box_blur
import matplotlib.pyplot as plt

def filtroBox(file):
    img = cv2.imread(file)
    plt.imshow(img)
    plt.title("Imagen original")
    plt.show()
    box_blur(img)   
  
def main(): #Metodo principal   
    ventana=tk.Tk() #Contenedor gráfico
    #Caracteriticas de la ventana:
    ventana.title("Filtro Tumblr")
    
    #Titulo y su formato
    titulo = tk.Label(ventana,font=("Arno Pro Smbd",24),fg="white",text= "Filtros Tumblr", bg="#556677",width=20, height=2)
    titulo.grid(row=0, column=1)
    
    l1 = tk.Label(ventana)
    l1.grid(row=1, column=1)
    
    T = tk.Entry(ventana, font=("Arno Pro Smbd",20))
    T.grid(row=2,column=1)

    l2 = tk.Label(ventana)
    l2.grid(row=3, column=1)

    #Se crea el boton aceptar que tiene la funcion de mandar al metodo opcion_elegida() la opcion y la caja de texto para realizar la tarea
    boton1 = tk.Button(ventana,font=("Arial",14), text="Filtro 1", command = lambda: filtroBox(T.get()))
    boton1.grid(row=4,column=1)

    l3 = tk.Label(ventana)
    l3.grid(row=5, column=1)

    #loop para mantener la ventana siempre visible
    ventana.mainloop()

#Se ejecuta la funcion principal
main()