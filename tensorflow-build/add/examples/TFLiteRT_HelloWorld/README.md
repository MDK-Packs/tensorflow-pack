# TensorFlow Lite RT Hello World Example

This reference application demonstrates how to use TensorFlow Lite for Microcontrollers with CMSIS support. The example trains and runs a small neural network that mimics a sine wave function.

## Prerequisites

- Visual Studio Code
- [Keil Studio Extensions](https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack) for VSCode
- Python 3.11.5 with Jupyter support and VSCode extension.
- Compatible development board providing STDIO interface

## Project Setup

1. Open the project folder in VSCode
2. VSCode will automatically detect this as a CMSIS project
3. In the CMSIS Project view:
   - Select a compatible board that provides STDIO interface
   - The board must have sufficient RAM for the application

### Memory Configuration

The application requires:
- **192KB Stack** 
- 64KB Heap

To **configure these requirements** you typically find Stack and Heap settings in either the startup code (Assembler Startup Code) or the linker script (C Startup Code).

## Training the Model

1. Navigate to `Training/train_TFL_Micro_hello_world_model.ipynb`
2. Open the Jupyter Notebook
3. Select your Python 3.11.5 kernel
4. Run all cells to:
   - Train the neural network
   - Generate the model
   - Copy model files to the Model layer

The notebook allows you to experiment with:
- Different model architectures
- Training parameters
- Data preprocessing

## Building and Running

In the CMSIS Project view:

1. Select your target board
2. Click "Build" to compile the project
3. Click "Run" to flash and execute
4. Monitor the output via the board's STDIO interface, which will display the deviation from an expected value.

``` bash
Tensorflow LiteRT Hello World!
(INFO) Profile Memory and Latency
(INFO) Load Float Model and Perform Inference
Δ [0] = 0.042087
Δ [1] = 0.023122
Δ [2] = 0.020444
Δ [3] = 0.024095
(INFO) Load Quantized Model and Perform Inference
Δ [0] = 0.047887
Δ [1] = 0.061695
Δ [2] = 0.040116
Δ [3] = 0.006767
~~~ALL TESTS PASSED~~~
```

## Project Structure

```
├── Source/
│   └── hello_world_test.cpp    # Main application code
├── Training/
│   └── train_TFL_Micro_hello_world_model.ipynb    # Model training
├── Model/
│   └── model.clayer.yml        # Model layer configuration
└── TFLiteRT_HelloWorld.cproject.yml    # Project configuration
```

## Compatibility

This reference application requires:
- Board with STDIO implementation
- Sufficient RAM (128KB minimum recommended)

## Troubleshooting

1. If build fails, verify:
   - Board layer is properly selected
   - Memory settings are configured
   - All required CMSIS packs are installed

2. If execution fails, check:
   - Serial connection to board
   - Memory allocation errors
   - Stack/heap configuration

## Further Development

- Modify the model in the Jupyter notebook
- Experiment with different neural network architectures
- Adjust memory settings based on your requirements
- Add custom preprocessing or postprocessing

## References

- [CMSIS Reference Applications](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/blob/main/docs/ReferenceApplications.md)
- [TensorFlow Lite for Microcontrollers](https://www.tensorflow.org/lite/microcontrollers)
