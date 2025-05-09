<?xml version="1.0" encoding="UTF-8"?>
<package schemaVersion="1.6" 
  xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="PACK.xsd">
  <vendor>tensorflow</vendor>
  <name>tensorflow-lite-micro</name>
  <description overview="Documentation/README.md">LiteRT, formerly known as TensorFlow Lite, is Google's high-performance runtime for on-device AI.</description>

  <url>https://github.com/MDK-Packs/tensorflow-pack/releases/download/%{RELEASE_VERSION}%/</url>
  <license>LICENSE</license>
  <repository type="git">https://github.com/MDK-Packs/tensorflow-pack.git</repository>
  <releases>
    <release version="%{RELEASE_VERSION}%" date="%{RELEASE_DATE}%"> Latest release. </release>
    %{HISTORY}%
  </releases>

  <requirements>
    <packages>
      <package name="CMSIS-NN" vendor="ARM" version="7.0.0:7.99.99"/>
      <package name="gemmlowp" vendor="tensorflow" version="%{RELEASE_VERSION}%:%{RELEASE_VERSION}%"/>
      <package name="flatbuffers" vendor="tensorflow" version="%{RELEASE_VERSION}%:%{RELEASE_VERSION}%"/>
      <package name="kissfft" vendor="tensorflow" version="%{RELEASE_VERSION}%:%{RELEASE_VERSION}%"/>
      <package name="ruy" vendor="tensorflow" version="%{RELEASE_VERSION}%:%{RELEASE_VERSION}%"/>
      <package name="ethos-u-core-driver" vendor="ARM" version="%{RELEASE_VERSION}%:%{RELEASE_VERSION}%"/>
    </packages>
  </requirements>

  <taxonomy>
    <description Cclass="Machine Learning">Software Components for Machine Learning</description>
  </taxonomy>

  <conditions>
    <condition id="CMSIS-NN">
        <require condition="Kernel Utils"/>
        <require condition="3rd Party"/>
        <require Cclass="CMSIS" Cgroup="NN Lib"/>
    </condition>
    <condition id="Reference">
        <require condition="Kernel Utils"/>
        <require condition="3rd Party"/>       
    </condition>
    <condition id="Ethos-U">
        <require condition="Kernel Utils"/>
        <require condition="3rd Party"/>
        <require Cclass="Machine Learning" Cgroup="NPU Support" Csub="Ethos-U Driver"/>
    </condition>
    <condition id="Kernel Utils">
        <require Cclass="Machine Learning" Cgroup="TensorFlow" Csub="Kernel Utils"/>
    </condition>
    <condition id="3rd Party">
      <require Cclass="Data Processing" Cgroup="Math" Csub="kissfft" Cvariant="tensorflow"/>
      <require Cclass="Data Processing" Cgroup="Math" Csub="ruy" Cvariant="tensorflow"/>
      <require Cclass="Data Processing" Cgroup="Math" Csub="gemmlowp fixed-point" Cvariant="tensorflow"/>
      <require Cclass="Data Exchange" Cgroup="Serialization" Csub="flatbuffers" Cvariant="tensorflow"/>
    </condition>    
  </conditions>

  <components>
    <component Cclass="Machine Learning" Cgroup="TensorFlow" Csub="Kernel" Cvariant="Reference" Cversion="%{RELEASE_VERSION}%" condition="Reference">
      <description>TensorFlow Lite Micro Library</description>
      <RTE_Components_h>
        <!-- the following content goes into file 'RTE_Components.h' -->
        #define RTE_ML_TF_LITE     /* TF */
      </RTE_Components_h>
      <Pre_Include_Global_h>
        // enabling global pre includes 
        #define TF_LITE_STATIC_MEMORY 1
      </Pre_Include_Global_h>
      <files>
        %{KERNEL_FILES_REFERENCE}%
        <file category="include" name="./"/>
      </files>
    </component>
    <component Cclass="Machine Learning" Cgroup="TensorFlow" Csub="Kernel" Cvariant="CMSIS-NN" Cversion="%{RELEASE_VERSION}%" condition="CMSIS-NN" >
      <description>TensorFlow Lite Micro Library</description>
      <RTE_Components_h>
        <!-- the following content goes into file 'RTE_Components.h' -->
        #define RTE_ML_TF_LITE     /* TF */
      </RTE_Components_h>
      <Pre_Include_Global_h>
        // enabling global pre includes 
        #define TF_LITE_STATIC_MEMORY 1
        #define CMSIS_NN
      </Pre_Include_Global_h>
      <files>
        %{KERNEL_FILES_CMSIS}%
        <file category="include" name="./"/>
      </files>
    </component>
    <component Cclass="Machine Learning" Cgroup="TensorFlow" Csub="Kernel" Cvariant="Ethos-U" Cversion="%{RELEASE_VERSION}%" condition="Ethos-U">
      <description>TensorFlow Lite Micro Library</description>
      <RTE_Components_h>
        <!-- the following content goes into file 'RTE_Components.h' -->
        #define RTE_ML_TF_LITE     /* TF */
      </RTE_Components_h>
      <Pre_Include_Global_h>
        // enabling global pre includes 
        #define TF_LITE_STATIC_MEMORY 1
        #define TF_LITE_DISABLE_X86_NEON 1
        //#define TF_LITE_STRIP_ERROR_STRINGS 1
        #define CMSIS_NN
      </Pre_Include_Global_h>
      <files>
         %{KERNEL_FILES_ETHOS}%
        <file category="include" name="./"/>
      </files>
    </component>
     <!-- this component can be merged into the Kernel components, when duplicate module name issue is solved elsewhere -->
    <component Cclass="Machine Learning" Cgroup="TensorFlow" Csub="Kernel Utils" Cversion="%{RELEASE_VERSION}%">
      <description>TensorFlow Lite Micro Library - Kernel Utilities</description>
      <files>
        <file category="sourceCpp" name="tensorflow/lite/kernels/kernel_util.cpp"/> 
        <file category="sourceCpp" name="tensorflow/lite/micro/system_setup.cpp" version="%{RELEASE_VERSION}%" attr="config"/>
        <file category="sourceCpp" name="tensorflow/lite/micro/cortex_m_generic/micro_time.cpp" version="%{RELEASE_VERSION}%" attr="config"/>
        <file category="sourceCpp" name="tensorflow/lite/micro/cortex_m_generic/debug_log.cpp" version="%{RELEASE_VERSION}%" attr="config"/>
        %{KERNEL_UTIL_FILES}%
      </files>
    </component>
    <component Cclass="Machine Learning" Cgroup="TensorFlow" Csub="Testing" Cversion="%{RELEASE_VERSION}%">
      <description>TensorFlow Lite Micro Test Utilities</description>
      <RTE_Components_h>
        <!-- the following content goes into file 'RTE_Components.h' -->
        #define RTE_ML_TF_LITE     /* TF */
      </RTE_Components_h>
      <files>
        %{TEST_FILES}%
        <file category="include" name="./"/>
      </files>
    </component>
    <component Cclass="Machine Learning" Cgroup="TensorFlow" Csub="Signal Library" Cvariant="Reference" Cversion="%{RELEASE_VERSION}%">
      <description>TensorFlow Lite Micro Signal Library</description>
      <RTE_Components_h>
        <!-- the following content goes into file 'RTE_Components.h' -->
        #define RTE_ML_TF_LITE     /* TF */
      </RTE_Components_h>
      <files>
        %{SIGNAL_FILES_REFERENCE}%
        <file category="include" name="./"/>
      </files>
    </component>
  </components>

  <examples>
    <example name="Tensorflow LiteRT HelloWorld" doc="README.md" folder="examples/TFLiteRT_HelloWorld">
      <description>TensorFlow LiteRT HelloWorld Example</description>
      <project>
        <environment name="csolution" load="TFLiteRT_HelloWorld.csolution.yml"/>
      </project>
    </example>
  </examples>

</package>
