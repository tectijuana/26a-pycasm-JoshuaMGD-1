/*
 * Autor: Joshua Daniel Moreno Gonzalez
 * Descripcion: Declaraciones de funciones en C y ARM64 Assembly
 * Fecha: 2026-04-14
 */

#ifndef OPS_H
#define OPS_H

#ifdef __cplusplus
extern "C" {
#endif

// Funciones implementadas en Assembly
int asm_sum(int a, int b);
int asm_sub(int a, int b);
int asm_max(int a, int b);
int asm_array_sum(int *arr, int n);
int asm_array_max(int *arr, int n);

// Wrappers en C
int c_sum(int a, int b);
int c_sub(int a, int b);
int c_max(int a, int b);
int c_array_sum(int *arr, int n);
int c_array_max(int *arr, int n);

#ifdef __cplusplus
}
#endif

#endif
