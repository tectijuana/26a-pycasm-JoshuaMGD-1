/*
 * Autor: Joshua Daniel Moreno Gonzalez
 * Descripcion: Funciones ARM64 Assembly para operaciones basicas
 * Fecha: 2026-04-14
 */

.text

.global asm_sum
.type asm_sum, %function
asm_sum:
    add w0, w0, w1
    ret

.global asm_sub
.type asm_sub, %function
asm_sub:
    sub w0, w0, w1
    ret

.global asm_max
.type asm_max, %function
asm_max:
    cmp w0, w1
    csel w0, w0, w1, ge
    ret

.global asm_array_sum
.type asm_array_sum, %function
asm_array_sum:
    // x0 = puntero al arreglo
    // w1 = tamaño n
    mov w2, #0          // i = 0
    mov w3, #0          // suma = 0

.Lsum_loop:
    cmp w2, w1
    bge .Lsum_done

    ldr w4, [x0, w2, sxtw #2]
    add w3, w3, w4
    add w2, w2, #1
    b .Lsum_loop

.Lsum_done:
    mov w0, w3
    ret

.global asm_array_max
.type asm_array_max, %function
asm_array_max:
    // x0 = puntero
    // w1 = n
    cmp w1, #0
    ble .Lmax_empty

    mov w2, #1
    ldr w3, [x0]        // max = arr[0]

.Lmax_loop:
    cmp w2, w1
    bge .Lmax_done

    ldr w4, [x0, w2, sxtw #2]
    cmp w4, w3
    csel w3, w4, w3, gt
    add w2, w2, #1
    b .Lmax_loop

.Lmax_done:
    mov w0, w3
    ret

.Lmax_empty:
    mov w0, #0
    ret
