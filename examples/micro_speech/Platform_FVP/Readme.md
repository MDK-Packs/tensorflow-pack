# Microspeech example for Corstone-300 FVP

This example shows how to run a 20 KB model that can recognize 2 keywords, "yes" and "no", from speech data. The code has a small footprint (for example, around 22 KB on a Cortex-M3) and only uses about 10 KB of RAM for working memory, so it's able to run on systems like an STM32F103 with only 20 KB of total SRAM and 64 KB of Flash.

The example is created and configured to work with the Corstone-300 free FVP (Fixed Virtual Platform) available from [Arm Ecosystems FVPs](developer.arm.com/free-fvps). Without an audio input channel, the FVP will run the tests for the example using predefined input buffers.

## How to build and run...

### ... on a docker container (any OS)

Requirements:
- [Docker](https://www.docker.com/get-started) installed on your computer.

Pull the docker image from [Dockerhub](https://hub.docker.com/) and instantiate a container on your machine. Make sure the `-v` parameter points to your local project folder:

```
docker run -i --mac-address="00:02:F7:FF:55:55" -v ~\projects\tensorflow-pack\Examples\micro_speech_test:/workspace/host --name tflm-container -d armswdev/cmsis_tools_m55:latest
```

Install the TensorFlow pack:

```
docker exec tflm-container cp_install.sh /workspace/host/Platform_FVP/packlist
```

Build the example using the following command:

```
docker exec tflm-container cbuild.sh /workspace/host/Platform_FVP/microspeech.cprj
```

Run the executable on the FVP in the container:

```
 docker exec tflm-container FVP_Corstone_SSE-300_Ethos-U55 -q --cyclelimit 100000000 -f /workspace/host/Platform_FVP/ARMCM55_config.txt /workspace/host/Platform_FVP/Objects/microspeech.axf
```

Note, that you might need to install [xterm](https://invisible-island.net/xterm/xterm.html) using the following command into your container once:

```
docker exec tflm-container apt install xterm -y
```

### ... in Keil MDK (Windows only)

Requirements:
- [Keil MDK 5.34 or higher](https://www.keil.com/demo/eval/arm.htm)
- Windows version of the ecosystem [FVP for Corstone-300 with Ethos-U55](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps). In case you use a custom installation folder for the FVP, you will need to reflect this in the example (**Options for Target - Debug - Settings for Models Armv8-M Debugger**)
- Download and install all Packs from the latest release on [GitHub](https://github.com/MDK-Packs/tensorflow-pack/releases/tag/preview-0.1).
- Clone of this repository to your local machine.
- Navigate to the `examples/micro_speech_test/Platform_FVP` folder.
- Open `microspeech.uvprojx` in µVision IDE.
- Make sure the "Example Test" target is selected from the dropdown menu on the menu bar.
- Now build the project using **Project - Build** and then use **Debug - Start Debugging**. Run the example by pressing F5. The simulation opens a terminal window with the STDIO output of the example.
