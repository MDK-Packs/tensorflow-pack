# LiteRT CMSIS Pack (tensorflow::tensorflow-lite-micro)

## Overview

The LiteRT CMSIS Pack integrates LiteRT (formerly TensorFlow Lite Micro) into the CMSIS ecosystem. This enables developers to seamlessly incorporate machine learning capabilities into embedded applications on ARM Cortex-M based microcontrollers, leveraging the familiar CMSIS-Pack format for straightforward software component management.

## Using the LiteRT stack

LiteRT (short for Lite Runtime), is Google's high-performance runtime for on-device AI. You can find ready-to-run LiteRT models for a wide range of ML/AI tasks, or convert and run TensorFlow, PyTorch, and JAX models to the TFLite format using the AI Edge conversion and optimization tools.

Refer to the official documentation to [Get Started with LiteRT in C++](https://ai.google.dev/edge/litert/inference#run-c) or check out the ["Hello World" Reference Application](https://github.com/MDK-Packs/tensorflow-pack/tree/main/tensorflow-build/add/examples/TFLiteRT_HelloWorld) that demonstrates a complete training and integration cycle.

## Components of the Pack

The LiteRT CMSIS Pack provides the LiteRT stack, offering flexibility and optimized performance across a range of Cortex-M devices through three distinct acceleration variants:

*   **Software Reference**: A baseline implementation for broad compatibility.
*   **CMSIS-NN**: Leverages optimized neural network kernels from the CMSIS-NN framework for significant performance gains on all Cortex-M processors.
*   **Ethos-U**: Enables hardware acceleration for compatible Arm Ethos-U Neural Processing Units (NPUs), delivering maximum performance and efficiency.

This approach ensures that developers can select the most appropriate variant for their specific hardware and performance requirements.

## Source and Versioning

The LiteRT stack originates from the official TensorFlow project ([https://github.com/tensorflow/tflite-micro](https://github.com/tensorflow/tensorflow)). Versioning of the LiteRT CMSIS Pack is closely aligned with LiteRT releases, ensuring access to the latest advancements and optimizations. Specific version details are provided within the pack and its release notes.

## Dependencies

The LiteRT CMSIS Pack relies on the following key software components - all are available as individual CMSIS Packs:

*   **CMSIS-DSP**: A collection of optimized digital signal processing functions, potentially utilized by machine learning models for tasks such as feature extraction.
*   **CMSIS-NN**: Provides highly optimized neural network kernels for ARM Cortex-M processors, crucial for achieving high-performance machine learning inference.
*   **Flatbuffers**: An efficient cross-platform serialization utility used for handling LiteRT models. 
*   **KissFFT**: A compact Fast Fourier Transform (FFT) component, sometimes used in audio processing or other signal processing tasks within ML applications.
*   **Ruy**: A matrix multiplication component, essential for many neural network operations.
*   **Ethos-U Driver (Optional)**: For systems incorporating an Arm Ethos-U NPU, this driver facilitates hardware-accelerated machine learning, enhancing performance and reducing power consumption.

## Examples

### Hello World Reference Application

The pack includes a "Hello World" example, which serves as a Reference Application. This demonstrates the fundamental integration and usage of the LiteRT stack. For more information on CMSIS Reference Applications, please see the [CMSIS Toolbox Reference Applications Documentation](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/blob/main/docs/ReferenceApplications.md).

*   **Purpose**: To verify the LiteRT stack setup and demonstrate basic inference capabilities on a target microcontroller.
*   **Functionality**: The application loads a simple, pre-trained model (here: sine wave prediction) and performs inference. Output is directed to a serial terminal via STDIO, allowing observation of the model's predictions.
*   **Training**: The model for the Hello World example can be trained using an included Jupyter Notebook, offering insight into the model creation process and a playground for model design experiments.

This Reference Application provides a clear starting point for developers integrating LiteRT into their projects.

#### API Interfaces

The LiteRT Reference Applications are hardware agnostic but requires API interfaces that are expressed using the csolution project connections: node. The reference applications in this pack consume the following API Interfaces. These interfaces should be provided by the board layer that is part of the Board Support Pack (BSP).


| Consumed API Interface | Description                                           |
|-------------------------|-------------------------------------------------------|
| **Hello World**        |                                                        |
| STDIN, STDOUT          | Standard I/O for user input and output via a console. |

