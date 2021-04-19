This is the tensorflow example "microspeech" for SSE-300 Fast Model (FVP) system.

This example shows how to run a 20 kB model that can recognize 2 keywords, "yes" and "no", from speech data. The code has a small footprint (for example, around 22 kilobytes on a Cortex M3) and only uses about 10 kilobytes of RAM for working memory, so it's able to run on systems like an STM32F103 with only 20 kilobytes of total SRAM and 64 kilobytes of Flash.

With the absence of an audio input channel, the FVP will actually run the tests for the example using predefined input buffers.

# How to build and run...

# ... on a docker container (any OS)

Requirements:
- Docker (https://www.docker.com/get-started)

Pull the docker image from Dockerhub and instance a container on your machine. Make sure the -v parameter points to your local project folder 
```
docker run -i --mac-address="00:02:F7:FF:55:55" -v ~\projects\tensorflow-pack\Examples\micro_speech_test:/workspace/host --name tflm-container -d armswdev/cmsis_tools_m55:latest
```

Install the tensorflow pack:

```
docker exec tflm-container cp_install.sh /workspace/host/Platform_FVP/packlist
```

Build the example using the following command:
```
docker exec tflm-container cbuild.sh /workspace/host/Platform_FVP/microspeech.cprj
```

Run the executable on the Fixed Virtual Platform:
```
 docker exec tflm-container FVP_Corstone_SSE-300_Ethos-U55 -q --cyclelimit 100000000 -f /workspace/host/Platform_FVP/ARMCM55_config.txt /workspace/host/Platform_FVP/Objects/microspeech.axf
```

Note, that you might need to install xterm using the following command into your container once:
```
docker exec tflm-container apt install xterm -y
```
# ... in Keil MDK (Windows)

Requirements:
- Keil MDK 5.34 or higher (https://www.keil.com/demo/eval/arm.htm)
- Ecosystem FVP for Corstone-300 with Ethos-U55 (https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps)

In case you use a custom installation folder for the FVP, you will need to reflect this in the example (Options for Target - Debug - Settings for Models Armv8-M Debugger)

Download and install all Packs from the latest release.
https://github.com/MDK-Packs/tensorflow-pack/releases/tag/preview-0.1

Get a clone of this repository to your local machine.

Navigate to the examples/microspeech_test/Platform_FVP folder.
Open microspeech.uvprojx in uVision IDE.

Make sure the "Example Test" target is selected from the dropdown menu on the menu bar.

Now build the project using Project - Build and then use Debug - Start Debugging. You can start the example by pressing F5. This will run the example in the simulation and open a terminal window with the STDIO output of the example.





