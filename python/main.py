"""
Autor: Joshua Daniel Moreno Gonzalez
Descripcion: Uso de ctypes para llamar una libreria .so compilada desde C/ASM
Fecha: 2026-04-14
"""

import ctypes
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB_PATH = os.path.join(BASE_DIR, "build", "libops.so")

lib = ctypes.CDLL(LIB_PATH)

# Firmas
lib.c_sum.argtypes = [ctypes.c_int, ctypes.c_int]
lib.c_sum.restype = ctypes.c_int

lib.c_sub.argtypes = [ctypes.c_int, ctypes.c_int]
lib.c_sub.restype = ctypes.c_int

lib.c_max.argtypes = [ctypes.c_int, ctypes.c_int]
lib.c_max.restype = ctypes.c_int

lib.c_array_sum.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
lib.c_array_sum.restype = ctypes.c_int

lib.c_array_max.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
lib.c_array_max.restype = ctypes.c_int


def py_sum(a, b):
    return a + b


def py_sub(a, b):
    return a - b


def py_max(a, b):
    return a if a >= b else b


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


def main():
    a, b = 15, 8
    values = [4, 7, 2, 9, 1, 8]
    n = len(values)

    IntArray = ctypes.c_int * n
    c_arr = IntArray(*values)

    print("=== Python ===")
    print("py_sum:", py_sum(a, b))
    print("py_sub:", py_sub(a, b))
    print("py_max:", py_max(a, b))
    print("py_array_sum:", py_array_sum(values))
    print("py_array_max:", py_array_max(values))

    print("\n=== C/ASM desde Python con ctypes ===")
    print("c_sum:", lib.c_sum(a, b))
    print("c_sub:", lib.c_sub(a, b))
    print("c_max:", lib.c_max(a, b))
    print("c_array_sum:", lib.c_array_sum(c_arr, n))
    print("c_array_max:", lib.c_array_max(c_arr, n))


if __name__ == "__main__":
    main()
