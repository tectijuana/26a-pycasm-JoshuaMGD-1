/*
 * Autor: Joshua Daniel Moreno Gonzalez
 * Descripcion: Wrappers en C para funciones ARM64 Assembly
 * Fecha: 2026-04-14
 */

#include "../include/ops.h"

int c_sum(int a, int b) {
    return asm_sum(a, b);
}

int c_sub(int a, int b) {
    return asm_sub(a, b);
}

int c_max(int a, int b) {
    return asm_max(a, b);
}

int c_array_sum(int *arr, int n) {
    return asm_array_sum(arr, n);
}

int c_array_max(int *arr, int n) {
    return asm_array_max(arr, n);
}
