"""
Autor: Joshua Daniel Moreno Gonzalez
Descripcion: Comparacion de rendimiento entre Python, C y ARM64 Assembly
Fecha: 2026-04-14
"""

import ctypes
import os
import random
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB_PATH = os.path.join(BASE_DIR, "build", "libops.so")

lib = ctypes.CDLL(LIB_PATH)

lib.c_sum.argtypes = [ctypes.c_int, ctypes.c_int]
lib.c_sum.restype = ctypes.c_int

lib.c_array_sum.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
lib.c_array_sum.restype = ctypes.c_int

lib.c_array_max.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
lib.c_array_max.restype = ctypes.c_int


def py_sum(a, b):
    return a + b


def py_array_sum(arr):
    total = 0
    for x in arr:
        total += x
    return total


def py_array_max(arr):
    if not arr:
        return 0
    m = arr[0]
    for x in arr:
        if x > m:
            m = x
    return m


def bench_binary_op(iterations=1_000_000):
    a, b = 25, 17

    t0 = time.perf_counter()
    for _ in range(iterations):
        py_sum(a, b)
    t1 = time.perf_counter()

    t2 = time.perf_counter()
    for _ in range(iterations):
        lib.c_sum(a, b)
    t3 = time.perf_counter()

    print("== Benchmark suma simple ==")
    print(f"Python : {t1 - t0:.6f} s")
    print(f"C/ASM  : {t3 - t2:.6f} s")
    print()


def bench_array_ops(size=100_000, repetitions=200):
    arr = [random.randint(1, 1000) for _ in range(size)]
    IntArray = ctypes.c_int * size
    c_arr = IntArray(*arr)

    t0 = time.perf_counter()
    for _ in range(repetitions):
        py_array_sum(arr)
    t1 = time.perf_counter()

    t2 = time.perf_counter()
    for _ in range(repetitions):
        lib.c_array_sum(c_arr, size)
    t3 = time.perf_counter()

    t4 = time.perf_counter()
    for _ in range(repetitions):
        py_array_max(arr)
    t5 = time.perf_counter()

    t6 = time.perf_counter()
    for _ in range(repetitions):
        lib.c_array_max(c_arr, size)
    t7 = time.perf_counter()

    print("== Benchmark arreglos ==")
    print(f"Python array_sum : {t1 - t0:.6f} s")
    print(f"C/ASM array_sum  : {t3 - t2:.6f} s")
    print(f"Python array_max : {t5 - t4:.6f} s")
    print(f"C/ASM array_max  : {t7 - t6:.6f} s")


if __name__ == "__main__":
    bench_binary_op()
    bench_array_ops()
