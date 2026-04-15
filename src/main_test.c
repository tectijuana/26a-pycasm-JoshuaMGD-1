/*
 * Autor: Joshua Daniel Moreno Gonzalez
 * Descripcion: Programa de prueba en C para funciones mixtas
 * Fecha: 2026-04-14
 */

#include <stdio.h>
#include "ops.h"

int main() {
    int arr[] = {4, 7, 2, 9, 1, 8};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("c_sum(10, 5) = %d\n", c_sum(10, 5));
    printf("c_sub(10, 5) = %d\n", c_sub(10, 5));
    printf("c_max(10, 5) = %d\n", c_max(10, 5));
    printf("c_array_sum(arr, n) = %d\n", c_array_sum(arr, n));
    printf("c_array_max(arr, n) = %d\n", c_array_max(arr, n));

    return 0;
}
