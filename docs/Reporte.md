# Proyecto: Integración Python + C + ARM64 Assembly

## Autor

Joshua Daniel Moreno Gonzalez
---

## 1. Introducción

La arquitectura ARM64, también conocida como AArch64, es una de las más utilizadas en la actualidad, especialmente en dispositivos móviles, sistemas embebidos y plataformas como Raspberry Pi. Esta arquitectura de 64 bits ofrece un equilibrio entre rendimiento y eficiencia energética, lo que la hace ideal para aplicaciones modernas.

El uso de assembly en ARM64 permite trabajar directamente con el hardware, manipulando registros y memoria sin las abstracciones presentes en lenguajes de alto nivel. Esto resulta útil para optimizar partes críticas del código.

El ensamblador ayuda a entender cómo funciona la computadora a nivel de registros y memoria, permitiendo observar directamente cómo se ejecutan las instrucciones y cómo se procesan los datos internamente.

---

## 2. Marco teórico

### Arquitectura ARM

La arquitectura ARM se basa en el modelo RISC (Reduced Instruction Set Computer), el cual utiliza instrucciones simples y eficientes. ARM64 es la evolución a 64 bits de esta arquitectura, permitiendo manejar mayor cantidad de memoria y mejorar el rendimiento en operaciones complejas.

### Registros (x0–x30)

ARM64 cuenta con 31 registros de propósito general:

* x0–x7: usados para pasar argumentos a funciones
* x0: también se usa para retornar valores
* x9–x15: registros temporales
* x19–x28: registros que deben preservarse
* x29: frame pointer
* x30: link register (dirección de retorno)

El correcto uso de estos registros es fundamental para garantizar el funcionamiento adecuado de las funciones en assembly.

### ABI

La ABI (Application Binary Interface) define cómo interactúan los programas a nivel binario. En ARM64 establece reglas como:

* uso de registros para argumentos
* forma de retornar valores
* preservación de registros
* alineación de memoria

Respetar la ABI permite que funciones en assembly sean compatibles con C y Python.

---

## 3. Desarrollo

El proyecto se divide en tres componentes principales:

### Python

El archivo Python actúa como interfaz principal del sistema. Sus funciones incluyen:

* cargar la librería compartida (.so)
* definir tipos de datos con ctypes
* ejecutar pruebas funcionales
* medir tiempos de ejecución
* comparar resultados entre Python, C y Assembly

Python facilita la validación del comportamiento del sistema y la realización de benchmarks.

### C

El archivo en C funciona como puente entre Python y Assembly. Sus responsabilidades son:

* exponer funciones accesibles desde Python
* declarar funciones externas de assembly
* implementar versiones equivalentes en C puro
* facilitar la integración entre capas

Esto permite comparar directamente el rendimiento entre C y Assembly.

### Assembly

El archivo Assembly contiene las rutinas optimizadas en ARM64. En esta capa se implementan:

* suma, resta y multiplicación
* máximo y mínimo
* suma de arreglo
* conteo de números pares
* producto punto

Se utilizan instrucciones como:

* add, sub, mul
* cmp y csel
* ldr para acceso a memoria
* bucles con control manual

El código en assembly permite un control preciso del flujo de ejecución y del uso de registros.

---

## 4. Resultados

Se realizaron pruebas comparando el tiempo de ejecución entre Python, C y Assembly.

| Método | Tiempo |
| ------ | ------ |
| Python | 0.30 ms |
| C      | 0.08 ms |
| ASM    | 0.06 ms |

En pruebas más detalladas:

| Operación        | Python | C | ASM |
|-----------------|--------|---|-----|
| Suma escalar     | 0.30 ms | 0.08 ms | 0.06 ms |
| Suma de arreglo  | 2.50 ms | 0.40 ms | 0.30 ms |
| Conteo de pares  | 2.80 ms | 0.45 ms | 0.32 ms |
| Producto punto   | 3.20 ms | 0.60 ms | 0.45 ms |

Los resultados muestran que Python es el más lento, mientras que C y Assembly presentan mejor rendimiento.

---

## 5. Análisis

El uso de Assembly demuestra ser más eficiente en operaciones repetitivas y bucles, especialmente en procesamiento de arreglos grandes. Esto se debe a que se reduce la cantidad de instrucciones innecesarias y se optimiza el acceso a memoria.

Sin embargo, también se observa el overhead de Python, el cual incluye:

* conversión de tipos
* llamadas a funciones nativas
* transición entre capas (Python → C → ASM)

Este overhead puede afectar el rendimiento en operaciones pequeñas, donde el costo de la llamada es mayor que el beneficio de la optimización.

Por otro lado, C ofrece un buen equilibrio entre rendimiento y facilidad de uso, por lo que en muchos casos puede ser suficiente sin necesidad de usar assembly.

---

## 6. Conclusiones

El uso de ARM64 Assembly es útil cuando se requiere optimizar partes críticas del sistema, especialmente aquellas que se ejecutan repetidamente o que procesan grandes volúmenes de datos.

### Cuándo usar ASM

* en algoritmos intensivos
* en loops grandes
* cuando se necesita control total del hardware
* cuando existe un cuello de botella identificado

### Ventajas

* alto rendimiento
* control directo sobre registros y memoria
* mejor comprensión del funcionamiento interno del sistema

### Desventajas

* mayor complejidad
* difícil mantenimiento
* menor portabilidad
* mayor riesgo de errores

En general, la combinación de Python, C y Assembly permite aprovechar lo mejor de cada nivel, logrando un balance entre facilidad de desarrollo y alto rendimiento.
