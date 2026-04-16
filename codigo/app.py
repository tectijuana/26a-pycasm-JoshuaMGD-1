# =========================================================
# app.py
# Carga la librería compartida con ctypes
# Ejecuta:
# - pruebas funcionales
# - benchmarks Python vs C vs ASM
# =========================================================

import ctypes
import os
import time
from statistics import mean

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LIB_PATH = os.path.join(BASE_DIR, "build", "libops.so")

if not os.path.exists(LIB_PATH):
    raise FileNotFoundError(f"No se encontró la librería: {LIB_PATH}")

lib = ctypes.CDLL(LIB_PATH)

Int64 = ctypes.c_longlong
UInt64 = ctypes.c_ulonglong
Int64Ptr = ctypes.POINTER(Int64)

# =========================================================
# Firmas de funciones C puras
# =========================================================
lib.c_add.argtypes = [Int64, Int64]
lib.c_add.restype = Int64

lib.c_sub.argtypes = [Int64, Int64]
lib.c_sub.restype = Int64

lib.c_mul.argtypes = [Int64, Int64]
lib.c_mul.restype = Int64

lib.c_max.argtypes = [Int64, Int64]
lib.c_max.restype = Int64

lib.c_min.argtypes = [Int64, Int64]
lib.c_min.restype = Int64

lib.c_sum_array.argtypes = [Int64Ptr, UInt64]
lib.c_sum_array.restype = Int64

lib.c_count_even.argtypes = [Int64Ptr, UInt64]
lib.c_count_even.restype = Int64

lib.c_dot_product.argtypes = [Int64Ptr, Int64Ptr, UInt64]
lib.c_dot_product.restype = Int64

# =========================================================
# Firmas de funciones ASM wrappers
# =========================================================
lib.asm_add_wrap.argtypes = [Int64, Int64]
lib.asm_add_wrap.restype = Int64

lib.asm_sub_wrap.argtypes = [Int64, Int64]
lib.asm_sub_wrap.restype = Int64

lib.asm_mul_wrap.argtypes = [Int64, Int64]
lib.asm_mul_wrap.restype = Int64

lib.asm_max_wrap.argtypes = [Int64, Int64]
lib.asm_max_wrap.restype = Int64

lib.asm_min_wrap.argtypes = [Int64, Int64]
lib.asm_min_wrap.restype = Int64

lib.asm_sum_array_wrap.argtypes = [Int64Ptr, UInt64]
lib.asm_sum_array_wrap.restype = Int64

lib.asm_count_even_wrap.argtypes = [Int64Ptr, UInt64]
lib.asm_count_even_wrap.restype = Int64

lib.asm_dot_product_wrap.argtypes = [Int64Ptr, Int64Ptr, UInt64]
lib.asm_dot_product_wrap.restype = Int64


# =========================================================
# Implementaciones Python puro
# =========================================================
def py_add(a, b):
    return a + b

def py_sub(a, b):
    return a - b

def py_mul(a, b):
    return a * b

def py_max(a, b):
    return a if a > b else b

def py_min(a, b):
    return a if a < b else b

def py_sum_array(arr):
    return sum(arr)

def py_count_even(arr):
    return sum(1 for x in arr if x % 2 == 0)

def py_dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))


# =========================================================
# Utilidades
# =========================================================
def to_c_array(py_list):
    return (Int64 * len(py_list))(*py_list)

def bench(func, *args, loops=10000, repeat=5):
    samples = []
    result = None

    for _ in range(repeat):
        t0 = time.perf_counter_ns()
        for _ in range(loops):
            result = func(*args)
        t1 = time.perf_counter_ns()
        samples.append((t1 - t0) / loops)

    return result, mean(samples)

def print_bench(title, py_func, c_func, asm_func, args, loops=10000):
    py_result, py_ns = bench(py_func, *args, loops=loops)
    c_result, c_ns = bench(c_func, *args, loops=loops)
    asm_result, asm_ns = bench(asm_func, *args, loops=loops)

    print(f"\n=== {title} ===")
    print(f"Resultado Python : {py_result}")
    print(f"Resultado C      : {c_result}")
    print(f"Resultado ASM    : {asm_result}")
    print(f"Tiempo Python    : {py_ns:,.2f} ns/llamada")
    print(f"Tiempo C         : {c_ns:,.2f} ns/llamada")
    print(f"Tiempo ASM       : {asm_ns:,.2f} ns/llamada")

    if c_ns > 0:
        print(f"Aceleración ASM vs C      : {c_ns / asm_ns:.2f}x")
    if py_ns > 0:
        print(f"Aceleración ASM vs Python : {py_ns / asm_ns:.2f}x")


# =========================================================
# Pruebas funcionales
# =========================================================
def run_tests():
    print("== PRUEBAS FUNCIONALES ==")

    a = 10
    b = 3

    print("Suma:")
    print(" Python:", py_add(a, b))
    print(" C     :", lib.c_add(a, b))
    print(" ASM   :", lib.asm_add_wrap(a, b))

    print("Resta:")
    print(" Python:", py_sub(a, b))
    print(" C     :", lib.c_sub(a, b))
    print(" ASM   :", lib.asm_sub_wrap(a, b))

    print("Multiplicación:")
    print(" Python:", py_mul(a, b))
    print(" C     :", lib.c_mul(a, b))
    print(" ASM   :", lib.asm_mul_wrap(a, b))

    print("Máximo:")
    print(" Python:", py_max(a, b))
    print(" C     :", lib.c_max(a, b))
    print(" ASM   :", lib.asm_max_wrap(a, b))

    print("Mínimo:")
    print(" Python:", py_min(a, b))
    print(" C     :", lib.c_min(a, b))
    print(" ASM   :", lib.asm_min_wrap(a, b))

    arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
    arr2 = [8, 7, 6, 5, 4, 3, 2, 1]

    c_arr1 = to_c_array(arr1)
    c_arr2 = to_c_array(arr2)

    print("Suma de arreglo:")
    print(" Python:", py_sum_array(arr1))
    print(" C     :", lib.c_sum_array(c_arr1, len(arr1)))
    print(" ASM   :", lib.asm_sum_array_wrap(c_arr1, len(arr1)))

    print("Conteo de pares:")
    print(" Python:", py_count_even(arr1))
    print(" C     :", lib.c_count_even(c_arr1, len(arr1)))
    print(" ASM   :", lib.asm_count_even_wrap(c_arr1, len(arr1)))

    print("Producto punto:")
    print(" Python:", py_dot_product(arr1, arr2))
    print(" C     :", lib.c_dot_product(c_arr1, c_arr2, len(arr1)))
    print(" ASM   :", lib.asm_dot_product_wrap(c_arr1, c_arr2, len(arr1)))


# =========================================================
# Benchmarks
# =========================================================
def run_benchmarks():
    print("\n== BENCHMARKS ==")

    a = 123456
    b = 7890

    print_bench(
        "Suma escalar",
        py_add,
        lib.c_add,
        lib.asm_add_wrap,
        (a, b),
        loops=100000
    )

    print_bench(
        "Resta escalar",
        py_sub,
        lib.c_sub,
        lib.asm_sub_wrap,
        (a, b),
        loops=100000
    )

    print_bench(
        "Multiplicación escalar",
        py_mul,
        lib.c_mul,
        lib.asm_mul_wrap,
        (a, b),
        loops=100000
    )

    arr1 = list(range(1, 10001))
    arr2 = list(range(10001, 20001))

    c_arr1 = to_c_array(arr1)
    c_arr2 = to_c_array(arr2)

    print_bench(
        "Suma de arreglo",
        py_sum_array,
        lambda x: lib.c_sum_array(c_arr1, len(arr1)),
        lambda x: lib.asm_sum_array_wrap(c_arr1, len(arr1)),
        (arr1,),
        loops=1000
    )

    print_bench(
        "Conteo de pares",
        py_count_even,
        lambda x: lib.c_count_even(c_arr1, len(arr1)),
        lambda x: lib.asm_count_even_wrap(c_arr1, len(arr1)),
        (arr1,),
        loops=1000
    )

    print_bench(
        "Producto punto",
        lambda _: py_dot_product(arr1, arr2),
        lambda _: lib.c_dot_product(c_arr1, c_arr2, len(arr1)),
        lambda _: lib.asm_dot_product_wrap(c_arr1, c_arr2, len(arr1)),
        (None,),
        loops=500
    )


if __name__ == "__main__":
    run_tests()
    run_benchmarks()
