# Displacements and reactions in springs elements with FEM
Cálculo de deformaciones y reacciones de elementos tipo resorte mediante el método de elemento finito

Usando como base el método de Ferreira:

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

con el fin de construir una matriz global 

```math
[k] [U] = [R]
```