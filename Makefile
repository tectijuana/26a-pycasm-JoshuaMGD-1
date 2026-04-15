# Autor: Joshua Daniel Moreno Gonzalez
# Descripcion: Compilacion del proyecto mixto Python + C + ARM64 Assembly
# Fecha: 2026-04-14

CC = gcc
CFLAGS = -Wall -Wextra -O2 -fPIC -Iinclude
LDFLAGS = -shared
BUILD_DIR = build
SRC_DIR = src
PY_DIR = python

LIB = $(BUILD_DIR)/libops.so
TEST = $(BUILD_DIR)/test_ops

C_SRC = $(SRC_DIR)/ops.c
ASM_SRC = $(SRC_DIR)/asm_ops.S
TEST_SRC = $(SRC_DIR)/main_test.c

all: dirs $(LIB) $(TEST)

dirs:
	mkdir -p $(BUILD_DIR)

$(LIB): $(C_SRC) $(ASM_SRC) include/ops.h
	$(CC) $(CFLAGS) $(LDFLAGS) -o $(LIB) $(C_SRC) $(ASM_SRC)

$(TEST): $(TEST_SRC) $(C_SRC) $(ASM_SRC) include/ops.h
	$(CC) $(CFLAGS) -o $(TEST) $(TEST_SRC) $(C_SRC) $(ASM_SRC)

run-c: all
	./$(TEST)

run-py: all
	python3 $(PY_DIR)/main.py

bench: all
	python3 $(PY_DIR)/benchmark.py

debug-c: all
	gdb ./$(TEST)

clean:
	rm -rf $(BUILD_DIR)

.PHONY: all dirs run-c run-py bench debug-c clean
