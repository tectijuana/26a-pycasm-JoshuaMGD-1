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

Se realizaron pruebas en una instancia ARM64 en AWS (EC2), ejecutando el proyecto mediante Python, C y Assembly.

A continuación se presentan los tiempos obtenidos:

| Método | Tiempo |
| ------ | ------ |
| Python | 104 ns |
| C      | 745 ns |
| ASM    | 742 ns |

En pruebas más detalladas:

| Operación        | Python (ns) | C (ns) | ASM (ns) |
|-----------------|------------|--------|----------|
| Suma escalar     | 104.25     | 747.89 | 744.49   |
| Resta escalar    | 103.66     | 736.48 | 738.89   |
| Multiplicación   | 104.47     | 745.07 | 741.05   |
| Suma de arreglo  | 74684.35   | 3378.79 | 9487.11 |
| Conteo de pares  | 527112.21  | 3540.02 | 10150.74 |
| Producto punto   | 861347.03  | 13670.31 | 13744.39 |

Los resultados muestran que:

- Python es más rápido en operaciones escalares simples.
- C y ASM superan ampliamente a Python en operaciones con arreglos.
- ASM no siempre es más rápido que C en este caso específico.
---

## 5. Análisis

Los resultados obtenidos presentan un comportamiento interesante y permiten entender mejor el rendimiento en distintos niveles de abstracción.

En primer lugar, se observa que Python es más rápido en operaciones escalares simples (como suma, resta y multiplicación). Esto se debe a que estas operaciones son ejecutadas directamente por el intérprete optimizado de Python, sin necesidad de cambiar de contexto hacia código nativo.

Por otro lado, las funciones implementadas en C y Assembly presentan mayor tiempo en estas operaciones pequeñas debido al overhead generado por ctypes, ya que cada llamada implica una transición entre Python, C y Assembly.

Sin embargo, en operaciones sobre arreglos grandes (como suma de arreglo, conteo de pares y producto punto), Python resulta significativamente más lento. En estos casos, C y Assembly son mucho más eficientes porque ejecutan bucles directamente en código compilado, evitando el overhead del intérprete.

Un aspecto importante es que Assembly no superó a C en todos los casos. Esto indica que el compilador (clang) ya realiza optimizaciones eficientes en C, y que el código Assembly aún puede optimizarse más para superar a C.

En resumen:

- Python es eficiente en operaciones simples.
- C es muy eficiente en procesamiento de datos.
- Assembly ofrece control total, pero requiere optimizaciones adicionales para superar al compilador.

Esto demuestra que el uso de Assembly debe enfocarse en secciones críticas donde el rendimiento sea realmente necesario.
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
