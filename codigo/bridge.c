/* =========================================================
 * bridge.c
 * Capa puente entre Python y ARM64 ASM
 *
 * Exporta:
 * 1) Implementaciones en C puro
 * 2) Implementaciones ASM accesibles desde Python
 *
 * Esto nos permite comparar:
 * Python vs C vs ASM
 * ========================================================= */

#include <stdint.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

/* =========================================================
 * Declaraciones de funciones Assembly
 * ========================================================= */
extern int64_t asm_add(int64_t a, int64_t b);
extern int64_t asm_sub(int64_t a, int64_t b);
extern int64_t asm_mul(int64_t a, int64_t b);
extern int64_t asm_max(int64_t a, int64_t b);
extern int64_t asm_min(int64_t a, int64_t b);
extern int64_t asm_sum_array(const int64_t *arr, uint64_t n);
extern int64_t asm_count_even(const int64_t *arr, uint64_t n);
extern int64_t asm_dot_product(const int64_t *a, const int64_t *b, uint64_t n);

/* =========================================================
 * Implementaciones C puras
 * ========================================================= */
int64_t c_add(int64_t a, int64_t b) {
    return a + b;
}

int64_t c_sub(int64_t a, int64_t b) {
    return a - b;
}

int64_t c_mul(int64_t a, int64_t b) {
    return a * b;
}

int64_t c_max(int64_t a, int64_t b) {
    return (a > b) ? a : b;
}

int64_t c_min(int64_t a, int64_t b) {
    return (a < b) ? a : b;
}

int64_t c_sum_array(const int64_t *arr, uint64_t n) {
    int64_t sum = 0;
    for (uint64_t i = 0; i < n; ++i) {
        sum += arr[i];
    }
    return sum;
}

int64_t c_count_even(const int64_t *arr, uint64_t n) {
    int64_t count = 0;
    for (uint64_t i = 0; i < n; ++i) {
        if ((arr[i] & 1LL) == 0) {
            count++;
        }
    }
    return count;
}

int64_t c_dot_product(const int64_t *a, const int64_t *b, uint64_t n) {
    int64_t acc = 0;
    for (uint64_t i = 0; i < n; ++i) {
        acc += a[i] * b[i];
    }
    return acc;
}

/* =========================================================
 * Wrappers ASM exportados a Python
 * Los nombres "asm_*_wrap" se exponen para evitar confusión
 * con los símbolos puros del archivo ops.s
 * ========================================================= */
int64_t asm_add_wrap(int64_t a, int64_t b) {
    return asm_add(a, b);
}

int64_t asm_sub_wrap(int64_t a, int64_t b) {
    return asm_sub(a, b);
}

int64_t asm_mul_wrap(int64_t a, int64_t b) {
    return asm_mul(a, b);
}

int64_t asm_max_wrap(int64_t a, int64_t b) {
    return asm_max(a, b);
}

int64_t asm_min_wrap(int64_t a, int64_t b) {
    return asm_min(a, b);
}

int64_t asm_sum_array_wrap(const int64_t *arr, uint64_t n) {
    return asm_sum_array(arr, n);
}

int64_t asm_count_even_wrap(const int64_t *arr, uint64_t n) {
    return asm_count_even(arr, n);
}

int64_t asm_dot_product_wrap(const int64_t *a, const int64_t *b, uint64_t n) {
    return asm_dot_product(a, b, n);
}

/* =========================================================
 * Modo standalone opcional:
 * permite crear un ejecutable nativo para GDB
 * sin agregar otro archivo al proyecto.
 * ========================================================= */
#ifdef BRIDGE_STANDALONE
int main(void) {
    int64_t arr1[] = {1, 2, 3, 4, 5, 6};
    int64_t arr2[] = {6, 5, 4, 3, 2, 1};
    uint64_t n = 6;

    printf("== PRUEBA NATIVA ==\n");
    printf("c_add(10, 3)            = %" PRId64 "\n", c_add(10, 3));
    printf("asm_add_wrap(10, 3)     = %" PRId64 "\n", asm_add_wrap(10, 3));

    printf("c_sub(10, 3)            = %" PRId64 "\n", c_sub(10, 3));
    printf("asm_sub_wrap(10, 3)     = %" PRId64 "\n", asm_sub_wrap(10, 3));

    printf("c_mul(10, 3)            = %" PRId64 "\n", c_mul(10, 3));
    printf("asm_mul_wrap(10, 3)     = %" PRId64 "\n", asm_mul_wrap(10, 3));

    printf("c_max(10, 3)            = %" PRId64 "\n", c_max(10, 3));
    printf("asm_max_wrap(10, 3)     = %" PRId64 "\n", asm_max_wrap(10, 3));

    printf("c_min(10, 3)            = %" PRId64 "\n", c_min(10, 3));
    printf("asm_min_wrap(10, 3)     = %" PRId64 "\n", asm_min_wrap(10, 3));

    printf("c_sum_array             = %" PRId64 "\n", c_sum_array(arr1, n));
    printf("asm_sum_array_wrap      = %" PRId64 "\n", asm_sum_array_wrap(arr1, n));

    printf("c_count_even            = %" PRId64 "\n", c_count_even(arr1, n));
    printf("asm_count_even_wrap     = %" PRId64 "\n", asm_count_even_wrap(arr1, n));

    printf("c_dot_product           = %" PRId64 "\n", c_dot_product(arr1, arr2, n));
    printf("asm_dot_product_wrap    = %" PRId64 "\n", asm_dot_product_wrap(arr1, arr2, n));

    return 0;
}
#endif
