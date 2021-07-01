
/*
 * Auto generated Run-Time-Environment Configuration File
 *      *** Do not modify ! ***
 *
 * Project: 'hello_world' 
 * Target:  'Example' 
 */

#ifndef RTE_COMPONENTS_H
#define RTE_COMPONENTS_H


/*
 * Define the Device Header File: 
 */
#define CMSIS_device_header "fsl_device_registers.h"

/* Keil.ARM Compiler::Compiler:I/O:STDOUT:User:1.2.0 */
#define RTE_Compiler_IO_STDOUT          /* Compiler I/O: STDOUT */
          #define RTE_Compiler_IO_STDOUT_User     /* Compiler I/O: STDOUT User */
/* NXP::Device:SDK Drivers:xip_board:2.0.1 */
#define XIP_EXTERNAL_FLASH 1
#define XIP_BOOT_HEADER_ENABLE 1
/* NXP::Device:SDK Drivers:xip_device:2.0.2 */
#define XIP_EXTERNAL_FLASH 1
#define XIP_BOOT_HEADER_ENABLE 1
/* NXP::Device:SDK Utilities:serial_manager_uart:1.0.0 */
#define SERIAL_PORT_TYPE_UART 1
/* tensorflow::Data Exchange:Serialization:flatbuffers:tensorflow:1.12.0 */
#define RTE_DataExchange_Serialization_flatbuffers     /* flatbuffers */
/* tensorflow::Data Processing:Math:gemmlowp fixed-point:tensorflow:1.0.0 */
#define RTE_DataExchange_Math_gemmlowp     /* gemmlowp */
/* tensorflow::Data Processing:Math:kissfft:tensorflow:1.4.5 */
#define RTE_DataExchange_Math_kissfft     /* kissfft */
/* tensorflow::Data Processing:Math:ruy:tensorflow:1.12.0 */
#define RTE_DataProcessing_Math_ruy     /* ruy */
/* tensorflow::Machine Learning:TensorFlow:Kernel:CMSIS-NN:0.2.20210628 */
#define RTE_ML_TF_LITE     /* TF */
/* tensorflow::Machine Learning:TensorFlow:Testing:0.2.20210628 */
#define RTE_ML_TF_LITE     /* TF */


#endif /* RTE_COMPONENTS_H */
