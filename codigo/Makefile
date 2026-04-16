# =========================================================
# Makefile profesional para proyecto ARM64 + C + Python
# =========================================================

CC       := clang
CFLAGS   := -Wall -Wextra -Werror -fPIC -O2
DBGFLAGS := -Wall -Wextra -Werror -fPIC -O0 -g
LDFLAGS  := -shared
BUILD    := build

LIB      := $(BUILD)/libops.so
OBJ_C    := $(BUILD)/bridge.o
OBJ_S    := $(BUILD)/ops.o
TEST_BIN := $(BUILD)/native_test

.PHONY: all debug clean run test gdb perf info dirs

all: dirs $(LIB) $(TEST_BIN)

debug: CFLAGS := $(DBGFLAGS)
debug: clean dirs $(LIB) $(TEST_BIN)

dirs:
	mkdir -p $(BUILD)

$(OBJ_C): bridge.c
	$(CC) $(CFLAGS) -c bridge.c -o $(OBJ_C)

$(OBJ_S): ops.s
	$(CC) $(CFLAGS) -c ops.s -o $(OBJ_S)

$(LIB): $(OBJ_C) $(OBJ_S)
	$(CC) $(LDFLAGS) -o $(LIB) $(OBJ_C) $(OBJ_S)

$(TEST_BIN): bridge.c ops.s
	$(CC) $(CFLAGS) -DBRIDGE_STANDALONE bridge.c ops.s -o $(TEST_BIN)

run: all
	python app.py

test: all
	./$(TEST_BIN)

gdb: debug
	gdb ./$(TEST_BIN)

perf: all
	perf stat ./$(TEST_BIN)

info:
	@echo "Arquitectura:"
	@uname -m
	@echo
	@echo "Compilador:"
	@$(CC) --version | head -n 1

clean:
	rm -rf $(BUILD)
