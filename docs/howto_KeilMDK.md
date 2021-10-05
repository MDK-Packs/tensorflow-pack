# Create a Tensorflow Lite Micro project in Keil MDK

To create a project in MDK Version 5, you must install the Device Family pack for the MCU you plan to use. 
While doing this, you will also install the tensorflow-lite-micro pack, that contains the latest tensorflow lite micro library.

Once you have done this, you may create a new project.

## Installing the Device Family Pack and the tensorflow pack
If you have not already done so, install the Device Family Pack (DFP) using the Pack Installer. To do this:

1. In uVision V5, click the Pack Installer icon.
2. On the left hand side, use the search field to type in the device name. You can either search for a board or device name. Both will 
filter the view on the right-hand side for the available packs. 
3. Click the Install Action button to the right of the DFP to install them.
4. Browse the "generic" list of packs on the Packs tab to find the tensorflow related packs. You should install the latest versions of all tensorflow::* packs.

![Pack Installer](https://github.com/MDK-Packs/tensorflow-pack/raw/main/docs/howto_KeilMDK_1.png)

## Creating a New Project
Follow the steps below to create a new MDK project using the Keil Run-Time Environment (RTE) and to specify and organize your source (and debug) files that are a part of this project.

1. Create a New Project File with the µVision menu command Project — New — µVision Project.
2. Select a microcontroller from the Device Database®. 
3. If you do don´t know which device to use yet, you can select the SSE-300-MPS3 device by Arm. 

SSE-300 is a reference SoC design by Arm based on the Cortex-M55 core. 
MDK can simulate this platform and no hardware will be required.
Once you selected the device the Runtime Environment Manager will be displayed. It allows to make a selection of software components used in your project.

4. Expand the Board support folder and select the board you will be using. Then:
5. Expand and select the components (File System, Graphics, Network, USB, etc.) you will be using in your application.
6. Make sure you select the Machine Learning::Tensorflow::Kernel* components.
7. Click the Resolve button to let µVision resolve as many required components based on your choices.

In Validation Output, double-click any missing components to display them, then select them for your application, until all missing components have been resolved.
Add your own Source Code to the project using the µVision editor (or any editor of your choice) by using one of the many ways to Add Source Files to Your Project.

## Add Hello World Source
