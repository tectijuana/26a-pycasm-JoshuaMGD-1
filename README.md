# Proyecto: Integración de Python, C y ARM64 Assembly

## Autor
Joshua Daniel Moreno Gonzalez

## Fecha de entrega
2026-04-16

## Descripción
Este proyecto integra Python, C y ARM64 Assembly para comprender la interacción entre lenguajes de alto y bajo nivel.  
Se utiliza una librería compartida `.so` junto con `ctypes` para llamar funciones compiladas desde Python.

## Objetivos
- Integrar Python con C y ARM64 Assembly
- Usar librerías compartidas `.so`
- Implementar funciones en Assembly
- Utilizar `ctypes` para la comunicación con Python
- Automatizar la compilación con Makefile
- Depurar con GDB
- Comparar rendimiento entre Python y código nativo

## Estructura del proyecto

```text
.
├── include
│   └── ops.h
├── src
│   ├── asm_ops.S
│   ├── main_test.c
│   └── ops.c
├── python
│   ├── benchmark.py
│   └── main.py
├── build
├── Makefile
└── README.md
```
## Funciones implementadas

### Operaciones básicas
- Suma  
- Resta  
- Máximo entre dos números  

### Operaciones con arreglos
- Suma de un arreglo  
- Máximo de un arreglo  

---

## Archivos principales

### `include/ops.h`
Contiene las declaraciones de las funciones implementadas en C y ARM64 Assembly.

### `src/asm_ops.S`
Contiene la implementación en ARM64 Assembly de:
- suma  
- resta  
- máximo  
- suma de arreglo  
- máximo de arreglo  

### `src/ops.c`
Contiene los wrappers en C que llaman a las funciones Assembly.

### `src/main_test.c`
Programa de prueba en C para validar el funcionamiento de las funciones.

### `python/main.py`
Carga la librería compartida con `ctypes` y ejecuta pruebas desde Python.

### `python/benchmark.py`
Realiza comparaciones de rendimiento entre Python y la librería nativa.

### `Makefile`
Automatiza la compilación, ejecución y depuración del proyecto.

---

## Compilación

```bash
make

