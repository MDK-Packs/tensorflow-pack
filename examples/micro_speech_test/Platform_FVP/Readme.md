This is the tensorflow example "microspeech" for SSE-300 Fast Model (FVP) system.

This example shows how to run a 20 kB model that can recognize 2 keywords, "yes" and "no", from speech data. The code has a small footprint (for example, around 22 kilobytes on a Cortex M3) and only uses about 10 kilobytes of RAM for working memory, so it's able to run on systems like an STM32F103 with only 20 kilobytes of total SRAM and 64 kilobytes of Flash.

With the absence of an audio input channel, the FVP will actually run the tests for the example using predefined input buffers.

# How to build and run...

# ... on a docker container (any OS)

Requirements:
- Docker (link)

Pull the docker image from Dockerhub and instance a container on your machine. Make sure the -v parameter points to your local project folder 
```
docker run -i -v ~\projects\tensorflow-pack\Examples:/workspace/host --name tflm-container -d armswdev/cmsis_tools_m55:lates
```

Install the tensorflow pack:

_todo_

Build the example using the following command:
```
docker exec tflm-container cbuild.sh /workspace/host/Platform_FVP/microspeech.cprj
```

Run the executable on the Fixed Virtual Platform:
```
 docker exec tflm-container FVP_Corstone_SSE-300 -q --cyclelimit 100000000 -f /workspace/host/Platform_FVP/ARMCM55_config.txt /workspace/host/Platform_FVP/Objects/microspeech.axf
```






# ... in Keil MDK (Windows)

Requirements:
- Keil MDK 5.35 or higher (link)
- Ecosystem FVP for Corstone-300 with Ethos-U55 (link)


