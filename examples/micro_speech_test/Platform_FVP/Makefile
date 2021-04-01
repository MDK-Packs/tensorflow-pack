#-------------------------------------------------------------------------------
# Copyright (c) 2020 Arm Limited. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#-------------------------------------------------------------------------------

PROJECT_NAME ?= Blinky
TARGET_ARCH ?= armv81

# Keil packs location
PACK_DIR ?= /home/$(USER)/.cache/arm/packs

SSE300_PACK := $(PACK_DIR)/ARM/V2M_MPS3_SSE_300_BSP/1.0.0
CMSIS_PACK := $(PACK_DIR)/ARM/CMSIS/5.7.0

OUTPUT_DIR = build
OBJ_DIR = $(OUTPUT_DIR)/obj

AR = armar
ASM = armasm
CC = armclang
LD = armlink
FROMELF = fromelf
SIZE = size

# Compiler flags
CC_FLAGS = --target=arm-arm-none-eabi -march=armv8.1-m.main+mve
CC_FLAGS += -fshort-wchar -O0 -D__thumb2__ -funsigned-char -gdwarf-3

# Assembler flags
ASM_FLAGS = --cpu=8-m.main

# Linker flags
LD_FLAGS = --strict --map --symbols --xref --cpu=8.1-M.Main.dsp
LD_FLAGS += --list=$(OUTPUT_DIR)/$(PROJECT_NAME).map --entry=Reset_Handler
LD_FLAGS += --info=summarysizes,sizes,totals,unused,veneers

# ========================= Common include folders =========================== #

# Include folders
INCLUDE_PATHS = -I. -I./API/Include -I./RTE/Device/SSE-300-MPS3 -I./RTE/_Target_1
INCLUDE_PATHS += -I$(SSE300_PACK)/Board/Device_Definition
INCLUDE_PATHS += -I$(SSE300_PACK)/Board/Platform
INCLUDE_PATHS += -I$(SSE300_PACK)/CMSIS_Driver/Config
INCLUDE_PATHS += -I$(SSE300_PACK)/CMSIS_Driver/Include
INCLUDE_PATHS += -I$(SSE300_PACK)/CMSIS_Driver
INCLUDE_PATHS += -I$(SSE300_PACK)/Device/Include
INCLUDE_PATHS += -I$(SSE300_PACK)/Native_Driver
INCLUDE_PATHS += -I$(CMSIS_PACK)/CMSIS/Include
INCLUDE_PATHS += -I$(CMSIS_PACK)/CMSIS/Driver/Include

# ============================ Linker script ================================= #

LINKER_SCRIPT_SELECT_FLAGS = --scatter=RTE/Device/SSE-300-MPS3/fvp_sse300_mps3_s.sct

# Flags for preprocessing the linker script
LD_PREPROC_FLAGS_COMMON =
LD_PREPROC_FLAGS = --predefine="$(LD_PREPROC_FLAGS_COMMON)"

# ============================ Project files ================================= #

C_FILES := $(shell find . -name "*.c")
C_FILES += $(shell find . -name "*.S")
C_FILES += $(shell find $(SSE300_PACK)/CMSIS_Driver -name "*.c")
C_FILES += $(shell find $(SSE300_PACK)/Device/Source -name "*.c")
C_FILES += $(shell find $(SSE300_PACK)/Native_Driver -name "*.c")
C_FILES += $(shell find $(SSE300_PACK)/Board/Device_Definition -name "*.c")

# ============================= Object files ================================= #

C_SOURCE_FILE_NAMES = $(notdir $(C_FILES))
C_PATHS = $(sort $(dir $(C_FILES)))
vpath %c $(C_PATHS)

OBJECTS = $(addprefix $(OBJ_DIR)/, $(C_SOURCE_FILE_NAMES:.c=.o))

TARGET_OUT = $(OUTPUT_DIR)/$(PROJECT_NAME).axf
TARGET_OUT_BIN = $(OUTPUT_DIR)/$(PROJECT_NAME).bin
TARGET_OUT_HEX = $(OUTPUT_DIR)/$(PROJECT_NAME).hex

# ======================== Makefile targets files ============================ #

all: $(OBJ_DIR) $(OBJECTS) $(TARGET_OUT) $(TARGET_OUT_BIN) size

# Create the object dir if that is not present
$(OBJ_DIR):
	mkdir -p -v $(OBJ_DIR)

# Compilation rules
$(OBJ_DIR)/%.o: %.c
	$(CC) -xc -std=c99 $(CC_FLAGS) $(INCLUDE_PATHS) -c -o $@ $<

$(OBJ_DIR)/%.o: %.S
	$(ASM) $(ASM_FLAGS) -o $@ $<

# Create axf binary
$(TARGET_OUT):
	$(LD) $(LD_FLAGS) $(LD_PREPROC_FLAGS) \
	      $(LINKER_SCRIPT_SELECT_FLAGS) --output=$(TARGET_OUT) \
	      $(addprefix $(OBJ_DIR)/, $(sort $(notdir $(OBJECTS))))

# Create bin
$(TARGET_OUT_BIN): $(TARGET_OUT)
	$(FROMELF) --bin --output=$(TARGET_OUT_BIN) $(TARGET_OUT)
	$(FROMELF) --i32combined --output=$(TARGET_OUT_HEX) $(TARGET_OUT)

size:
	$(SIZE) $(TARGET_OUT)

clean:
	rm -rf $(OUTPUT_DIR)

.PHONY: $(TARGET_OUT)
