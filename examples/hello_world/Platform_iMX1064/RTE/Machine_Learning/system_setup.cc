/* Copyright 2021 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#include "tensorflow/lite/micro/system_setup.h"

#include <stdint.h>

/* Prototypes */
extern "C" uint32_t LPUART1_GetFreq    (void);
extern "C" void     LPUART1_InitPins   (void);
extern "C" void     LPUART1_DeinitPins (void);
extern "C" uint32_t LPUART3_GetFreq    (void);
extern "C" void     LPUART3_InitPins   (void);
extern "C" void     LPUART3_DeinitPins (void);

#include "clock_config.h"
#include "board.h"
#include "pin_mux.h"
#include "fsl_iomuxc.h"

#include <stdio.h>

#include "tensorflow/lite/micro/cortex_m_generic/debug_log_callback.h"
	
namespace tflite {

// Callbacks for LPUART1 Driver
uint32_t LPUART1_GetFreq   (void) { return BOARD_BOOTCLOCKRUN_UART_CLK_ROOT; }
void     LPUART1_InitPins  (void) { /* Done in BOARD_InitDEBUG_UART function */ }
void     LPUART1_DeinitPins(void) { /* Not implemented */ }

// Callbacks for LPUART3 Driver
uint32_t LPUART3_GetFreq   (void) { return BOARD_BOOTCLOCKRUN_UART_CLK_ROOT; }
void     LPUART3_InitPins  (void) { /* Done in BOARD_InitARDUINO_UART function */ }
void     LPUART3_DeinitPins(void) { /* Not implemented */ }

void debug_log_printf(const char* s) {
		printf("%s", s);
}

// To add an equivalent function for your own platform, create your own
// implementation file, and place it in a subfolder named after the target. See
// tensorflow/lite/micro/debug_log.cc for a similar example.
void InitializeTarget() {
  
	BOARD_InitBootPins();
  BOARD_InitBootClocks();
  BOARD_InitDebugConsole();

  // GPIO_B1_10 is configured as ENET_REF_CLK
  // Software Input On Field: Force input path of pad GPIO_B1_10
  IOMUXC_SetPinMux(IOMUXC_GPIO_B1_10_ENET_REF_CLK, 1U);

  // Enable ENET_REF_CLK output mode
  IOMUXC_EnableMode(IOMUXC_GPR, kIOMUXC_GPR_ENET1TxClkOutputDir, true);

  NVIC_SetPriority(ENET_IRQn,    8U);
  NVIC_SetPriority(USDHC1_IRQn,  8U);
  NVIC_SetPriority(LPUART3_IRQn, 8U);

  SystemCoreClockUpdate();	
	
  RegisterDebugLogCallback(debug_log_printf);
}	

}  // namespace tflite
