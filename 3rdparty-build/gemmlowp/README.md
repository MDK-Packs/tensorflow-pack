# gemmlowp
This is an add-on to Google's [gemmlowp](https://github.com/google/gemmlowp) repository.
It adds a [PDSC file](https://arm-software.github.io/CMSIS_5/Pack/html/packFormat.html), so
that gemmlowp can be used in IDEs that support [CMSIS-Packs](https://arm-software.github.io/CMSIS_5/Pack/html/index.html).

## Directory Structure

| Directory            | Content                                                   |                
|:-------------------- |:--------------------------------------------------------- |
| contributions           | PDSC file required for pack build                 |

## Build
To build the pack, run the [gen_pack.sh](gen_pack.sh) script.

## Other related GitHub repositories

| Repository                  | Description                                               |                
|:--------------------------- |:--------------------------------------------------------- |
| [CMSIS](https://github.com/ARM-software/cmsis_5)    |  CMSIS  |
| [CMSIS-FreeRTOS](https://github.com/arm-software/CMSIS-FreeRTOS)            | CMSIS-RTOS adoption of FreeRTOS                                                      |
| [CMSIS-Driver](https://github.com/arm-software/CMSIS-Driver)                | Generic MCU driver implementations and templates for Ethernet MAC/PHY and Flash.  |
| [mdk-packs](https://github.com/mdk-packs)                                   | IoT cloud connectors as trail implementations for MDK (help us to make it generic)|
