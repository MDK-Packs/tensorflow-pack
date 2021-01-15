# Version: 0.10.0
# Date: 2020-12-28
# This file maps the CMSIS project options to toolchain settings.
#
#   - Applies to toolchain: ARMCC GCC 10.2.1

############### EDIT BELOW ###############
# Set base directory of toolchain
TOOLCHAIN_ROOT:= /workspace/gcc-arm-none-eabi-10-2020-q4-major/bin/
PREFIX=arm-none-eabi-

############ DO NOT EDIT BELOW ###########
AS:=$(TOOLCHAIN_ROOT)/$(PREFIX)as
CC:=$(TOOLCHAIN_ROOT)/$(PREFIX)gcc
CXX:=$(TOOLCHAIN_ROOT)/$(PREFIX)g++
LD:=$(TOOLCHAIN_ROOT)/$(PREFIX)gcc
AR:=$(TOOLCHAIN_ROOT)/$(PREFIX)ar
OC:=$(TOOLCHAIN_ROOT)/$(PREFIX)objcopy

# Escape whitespace in toolchain root
TOOLCHAIN_ROOT_WS:=$(subst $() ,\ ,$(TOOLCHAIN_ROOT))

# Assembler

ifeq ($(CPU),Cortex-M0)
  GNUASM_CPU:=-mcpu=cortex-m0
else ifeq ($(CPU),Cortex-M0+)
  GNUASM_CPU:=-mcpu=cortex-m0plus
else ifeq ($(CPU),Cortex-M1)
  GNUASM_CPU:=-mcpu=cortex-m1
else ifeq ($(CPU),Cortex-M3)
  GNUASM_CPU:=-mcpu=cortex-m3
else ifeq ($(CPU),Cortex-M4)
  ifeq ($(FPU),SP_FPU)
    GNUASM_CPU:=-mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard
  else
    GNUASM_CPU:=-mcpu=cortex-m4
  endif
else ifeq ($(CPU),Cortex-M7)
  ifeq ($(FPU),DP_FPU)
    GNUASM_CPU:=-mcpu=cortex-m7 -mfpu=fpv5-d16 -mfloat-abi=hard
  else ifeq ($(FPU),SP_FPU)
    GNUASM_CPU:=-mcpu=cortex-m7 -mfpu=fpv5-sp-d16 -mfloat-abi=hard
  else
    GNUASM_CPU:=-mcpu=cortex-m7
  endif
else ifeq ($(CPU),Cortex-M23)
  GNUASM_CPU:=-mcpu=cortex-m23
else ifeq ($(CPU),Cortex-M33)
  ifeq ($(FPU),SP_FPU)
    GNUASM_CPU:=-mcpu=cortex-m33 -mfpu=fpv5-sp-d16 -mfloat-abi=hard
  else ifeq ($(DSP),DSP)
    GNUASM_CPU:=-mcpu=cortex-m33
  else
    GNUASM_CPU:=-mcpu=cortex-m33+nodsp
  endif
else ifeq ($(CPU),Cortex-M35P)
  ifeq ($(FPU),SP_FPU)
    GNUASM_CPU:=-mcpu=cortex-m35p -mfpu=fpv5-sp-d16 -mfloat-abi=hard
  else ifeq ($(DSP),DSP)
    GNUASM_CPU:=-mcpu=cortex-m35p
  else
    GNUASM_CPU:=-mcpu=cortex-m35p+nodsp
  endif
else ifeq ($(CPU),Cortex-M55)
  ifeq ($(FPU),SP_FPU)
    GNUASM_CPU:=-mcpu=cortex-m55 -mfpu=fpv5-sp-d16 -mfloat-abi=hard
  else ifeq ($(DSP),DSP)
    GNUASM_CPU:=-mcpu=cortex-m55
  else
    GNUASM_CPU:=-mcpu=cortex-m55+nodsp
  endif
endif
ifndef GNUASM_CPU
$(error Error: CPU is not supported!)
endif

# Assembler

AS_CPU:=$(GNUASM_CPU)

AS_DEFINES:=$(call ews_patsubst,%,--defsym %=1,$(DEFINES))

ifeq ($(BYTE_ORDER),Little-endian)
  AS_BYTE_ORDER:=-mlittle-endian
else ifeq ($(BYTE_ORDER),Big-endian)
  AS_BYTE_ORDER:=-mbig-endian
endif

AS_FILE:=@

AS_FLAGS=

# C Compiler

CC_CPU:=$(GNUASM_CPU)

CC_DEFINES:=$(call patsubst,%,-D%,$(DEFINES))
_I:=-I
_PI:=-include 
_ISYS:=-isystem

ifeq ($(BYTE_ORDER),Little-endian)
  CC_BYTE_ORDER:=-mlittle-endian
else ifeq ($(BYTE_ORDER),Big-endian)
  CC_BYTE_ORDER:=-mbig-endian
endif

ifeq ($(SECURE),Secure)
  CC_SECURE:=-mcmse
else
  CC_SECURE:=
endif

CC_FILE:=@

CC_FLAGS:=\
-c\
-MD

CC_SYS_INC_PATH:=\
$(TOOLCHAIN_ROOT_WS)/../lib/gcc/arm-none-eabi/10.2.1/include\
$(TOOLCHAIN_ROOT_WS)/../lib/gcc/arm-none-eabi/10.2.1/include-fixed\
$(TOOLCHAIN_ROOT_WS)/../arm-none-eabi/include

# C++ Compiler

CXX_CPU:=$(CC_CPU)
CXX_DEFINES:=$(CC_DEFINES)
CXX_BYTE_ORDER:=$(CC_BYTE_ORDER)
CXX_SECURE:=$(CC_SECURE)
CXX_FILE:=$(CC_FILE)
CXX_FLAGS:=$(CC_FLAGS)

CXX_SYS_INC_PATH:=\
$(TOOLCHAIN_ROOT_WS)/../arm-none-eabi/include/c++/10.2.1\
$(TOOLCHAIN_ROOT_WS)/../arm-none-eabi/include/c++/10.2.1/arm-none-eabi\
$(TOOLCHAIN_ROOT_WS)/../arm-none-eabi/include/c++/10.2.1/backward\
$(CC_SYS_INC_PATH)

# Linker

LD_CPU:=$(GNUASM_CPU)

ifdef LD_SCRIPT
  LD_SCRIPT:=-T "$(LD_SCRIPT)"
endif

LD_FILE:=@

LD_FLAGS=\
-Xlinker -Map="$(subst \,,$(OUT_DIR)/$(TARGET)).map"

# Archiver

AR_FILE:=@

AR_FLAGS=\
rcs

# Target output

TARGET_LIB:=$(OUT_DIR)/lib$(TARGET).a
TARGET_ELF:=$(OUT_DIR)/$(TARGET).elf

# ELF to HEX conversion
ELF2HEX:=\
-O ihex "$(subst \,,$(TARGET_ELF))" "$(subst \,,$(TARGET_ELF:.elf=.hex))"

# ELF to BIN conversion
ELF2BIN:=\
-O binary "$(subst \,,$(TARGET_ELF))" "$(subst \,,$(TARGET_ELF:.elf=.bin))"
