# Displacements and reactions in springs elements with FEM

<p align="center">
  <img src="https://i.imgur.com/Qcqf36i.png" width=150/>
</p>

Cálculo de deformaciones y reacciones de elementos tipo resorte mediante el método de elemento finito

Este método implica considerar la relación del módulo elastico, las reacciones y las deformaciones de los resortes en base a la siguiente ecuación:

```math
\left\{
	\begin{array}{rcl}
		R_{n1} \\ R_{n2}
	\end{array}
\right\} 
= 
k_n
\begin{bmatrix}
	1 & -1 \\ -1 & 1
\end{bmatrix}
\left\{
	\begin{array}{rcl}
		U_{n1} \\ U_{n2}
	\end{array}
\right\} 
```

con el fin de construir una matriz global `[K]` que almacene todos los valores de $k$

```math
[K] [U] = [R]
```

## Script de Scilab

El código [springs](springs.sce) permite obtener la matriz global $k$ así como las reacciones y las deformaciónes para cada elemento. Al ejecutar el script dentro de scilab es necesario llenar los datos que este pide:

1. El número de resortes del sistema.
2. La cantidad de nodos que conforman el sistema.
3. La cantidad de fuerzas que interactuan con el sistema
4. Cada una de las fuerzas aplicadas al sistema,
5. y el nodo en el que se aplica.
6. Si los módulos elasticos son iguales para todo el sistema.
	- Al responder `no` el  script pedirá los módulos de cada resorte.
	- De no ser así el sistema pedirá unicamente un solo valor de $k$.
7. Los nodos a los que se conecta cada resorte.
8. Las nodos que se encuentran empotrados.



<details>
<summary> Ejemplo </summary>
## Ejemplo

![](https://i.imgur.com/XQX9pfM.png)

Tomando como ejemplo la siguiente imagen, tenemos un sistema de:
- 4 resortes
- 5 nodos
- 1 fuerza en el nodo 3
- 4 módulos elasticos
- Los nodos 1, 4 y 5 como condiciones de frontera.
- Resortes:

|No.| Nodo A | Nodo B |
|:--|:--|:--|
| 1 | 1 | 2 |
| 2 | 2 | 3 |
| 3 | 3 | 4 |
| 4 | 3 | 5 |

Suponiendo los siguientes valores:
- Fuerza: 16 N
- Resortes:

|No.| k |
|:--|:--|
| 1 |  2 |
| 2 |  7 |
| 3 | 12 |
| 4 |  1 |
 
**El sistema arroja los siguientes resultados**:

```shell
  "K"
   2.  -2.   0.    0.    0.
  -2.   9.  -7.    0.    0.
   0.  -7.   20.  -12.  -1.
   0.   0.  -12.   12.   0.
   0.   0.  -1.    0.    1.
  "U"
   0.
   0.8549618
   1.0992366
   0.
   0.
  "R"
  -1.7099237
   0.
   16.000000
  -13.190840
  -1.0992366
```

donde $U$ son los desplazamientos y $R$ las reacciones en cada nodo.
</details>

# Interfaz de Python

![](https://i.imgur.com/iHRarJf.png)

La interfaz grafica permite obtener los mismos datos usando numpy

## Librerías necesarias

- sys, json
- notify-py
- pyperclip
- PySide6
- numpy

```bash
pip install -r requirements.txt
```

## Características
- Adaptable a la cantidad de resortes y fuerzas del sistema a analizar.
- Muestra los resultados en ventanas separadas.
- Permite copiar los datos al portapapeles.

#### En proceso

> [!TIP]
> - Agregar unidades