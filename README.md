<a href="#">
    <img src="https://javier.rodriguez.org.mx/itesm/2014/tecnologico-de-monterrey-black.png" alt="ITESM" title="ITESM" align="right" height="60" />
</a>

# EQ8_TC1001S 🚀

## Propuesta de proyecto ⚙️
Como parte de nuestro proyecto, para identificar una buena propuesta, sé planteo la siguiente **aplicación**:

---

  La detección de bordes es un proceso muy importante en la industria de la metrología ya que define los límites para la medición. La precisión en la detección del borde mejora la calidad en los procesos que se realicen.
### ¿Por qué? 🤔
La razón por a cuál se utilizará el filtro *edge detection* es que nuestro equipo considera que este permite extraer información importante para la medición. Utilizando la detección de bordes es posible obtener las figuras o líneas que se tomarán en cuanta para medir, sin que sufran de algún efecto por los colores alrededor.

Imagen de Kernel 3x3
![](https://aishack.in/static/img/tut/conv-edge-detection.jpg)

## Uso del proyecto

---

### Prerrequisitos

Le proyecto está programado en el lenguaje python, este puede ser descargado de la siguiente liga: https://www.python.org/downloads/, y posteriormente ser agregado al PATH de la computadora. Además de python es necesario instalar ciertas librerías para asegurar que el script funcione adecuadamente, esto se puede realizar utilizando PIP. Las librerías de python necesarias son las siguientes:

* OpenCV
```sh
	pip install opencv-python
```
* Numpy
```sh
	pip install numpy
```
* Matplotlib
```sh
	pip install matplotlib
```
* Argparse
```sh
	pip install argparse
```
* Tkinter (normalmente se insatla automáticamente con Python)
```sh
	pip install tk
```

### Corrida
Usando la línea de comandos es necesario posicionarse en la carpeta del proyecto, para ello se puede utilizar el comando cd, un ejemplo sería:
```sh
	cd C:\Users\usr\Proyectos\EQ8_TC1001S
```

Posteriormente, para correr el script se debe ingresar el siguiente comando en la terminal que se esté usando:

```sh
	python main_root.py
```

Al correr el programa, se desplegará una ventana similar a la siguiente:
**Aqui va una imagen**

En la casilla se debe ingresar el nombre de la imagen que se desee utilizar para aplicar los diferentes filtros. Utilizando la imagen incluída de prueba, esto se vería de la siguiente manera:
**Aquí va otra imagen**

Finalmente, solo es necesario hacer clic sobre el botón que se desee para aplicar dicho filtro sobre la imagen (transformada a escala de grises si es necesario), esto generará una ventana emergente con la imagen nueva.

## Autores ✒️
---
Este proyecto es realizado para la Semana TEC "Herramientas computacionales: el arte de la programación (Gpo 120)" por :
* Ian García - A01706892
* Emiliano Vásquez Olea- A01707035
* José Ángel Rico Mendieta - A01707404

---

## Referencias

---