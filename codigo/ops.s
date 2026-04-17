/* =========================================================
 * ops.s
 * Rutinas ARM64 (AArch64) optimizadas
 *
 * ABI AArch64:
 * - x0-x7  : argumentos / retorno en x0
 * - x19-x28: callee-saved (si se usan, deben preservarse)
 *
 * Aquí usamos solo registros temporales caller-saved
 * para no tener que salvar/restaurar estado adicional.
 * ========================================================= */

    .text

/* ---------------------------------------------------------
 * int64_t asm_add(int64_t a, int64_t b)
 * x0 = a
 * x1 = b
 * retorno x0 = a + b
 * --------------------------------------------------------- */
    .global asm_add
    .type asm_add, %function
asm_add:
    add x0, x0, x1
    ret

/* ---------------------------------------------------------
 * int64_t asm_sub(int64_t a, int64_t b)
 * x0 = a
 * x1 = b
 * retorno x0 = a - b
 * --------------------------------------------------------- */
    .global asm_sub
    .type asm_sub, %function
asm_sub:
    sub x0, x0, x1
    ret

/* ---------------------------------------------------------
 * int64_t asm_mul(int64_t a, int64_t b)
 * x0 = a
 * x1 = b
 * retorno x0 = a * b
 * --------------------------------------------------------- */
    .global asm_mul
    .type asm_mul, %function
asm_mul:
    mul x0, x0, x1
    ret

/* ---------------------------------------------------------
 * int64_t asm_max(int64_t a, int64_t b)
 * Usa selección condicional para evitar salto explícito
 * --------------------------------------------------------- */
    .global asm_max
    .type asm_max, %function
asm_max:
    cmp x0, x1
    csel x0, x0, x1, ge
    ret

/* ---------------------------------------------------------
 * int64_t asm_min(int64_t a, int64_t b)
 * --------------------------------------------------------- */
    .global asm_min
    .type asm_min, %function
asm_min:
    cmp x0, x1
    csel x0, x0, x1, le
    ret

/* ---------------------------------------------------------
 * int64_t asm_sum_array(const int64_t *arr, uint64_t n)
 * x0 = arr
 * x1 = n
 *
 * retorno x0 = suma total
 * --------------------------------------------------------- */
    .global asm_sum_array
    .type asm_sum_array, %function
asm_sum_array:
    cbz x1, .sum_done_zero

    mov x2, x0          // x2 = puntero actual
    mov x3, x1          // x3 = contador
    mov x0, #0          // acumulador

.sum_loop:
    ldr x4, [x2], #8    // cargar int64_t y avanzar puntero
    add x0, x0, x4
    subs x3, x3, #1
    b.ne .sum_loop
    ret

.sum_done_zero:
    mov x0, #0
    ret

/* ---------------------------------------------------------
 * int64_t asm_count_even(const int64_t *arr, uint64_t n)
 * cuenta elementos pares
 *
 * par si (valor & 1) == 0
 * --------------------------------------------------------- */
    .global asm_count_even
    .type asm_count_even, %function
asm_count_even:
    cbz x1, .even_done_zero

    mov x2, x0          // puntero
    mov x3, x1          // contador elementos
    mov x0, #0          // contador pares

.even_loop:
    ldr x4, [x2], #8
    and x5, x4, #1
    cmp x5, #0
    cinc x0, x0, eq     // x0 = x0 + 1 si eq
    subs x3, x3, #1
    b.ne .even_loop
    ret

.even_done_zero:
    mov x0, #0
    ret

/* ---------------------------------------------------------
 * int64_t asm_dot_product(const int64_t *a,
 *                         const int64_t *b,
 *                         uint64_t n)
 *
 * x0 = a
 * x1 = b
 * x2 = n
 * retorno x0 = sum(a[i] * b[i])
 * --------------------------------------------------------- */
    .global asm_dot_product
    .type asm_dot_product, %function
asm_dot_product:
    cbz x2, .dot_done_zero

    mov x3, x0          // ptr a
    mov x4, x1          // ptr b
    mov x5, x2          // contador
    mov x0, #0          // acumulador

.dot_loop:
    ldr x6, [x3], #8
    ldr x7, [x4], #8
    mul x6, x6, x7
    add x0, x0, x6
    subs x5, x5, #1
    b.ne .dot_loop
    ret

.dot_done_zero:
    mov x0, #0
    ret
