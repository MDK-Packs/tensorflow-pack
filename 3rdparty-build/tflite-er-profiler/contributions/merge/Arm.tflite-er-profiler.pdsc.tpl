<?xml version="1.0" encoding="UTF-8"?>
<package schemaVersion="1.6" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="PACK.xsd">
  <vendor>Arm</vendor>
  <name>tflite-er-profiler</name>
  <description>Event Recorder MicroProfiler for TensorFlow</description>
  <!-- web download link -->
  <url>https://review.mlplatform.org/</url>
  <license>LICENSE.txt</license>
  <releases>
    <release version="%{RELEASE_VERSION}%" date="%{RELEASE_DATE}%">
      EventRecorder Profiler for TensorFlow %{RELEASE_VERSION}%
    </release>
  </releases>
  <components>
    <component Cclass="Machine Learning" Cgroup="Tensorflow" Csub="Profiler" Cvariant="Event Recorder" Cversion="1.0.0">
      <description>Event Recorder MicroProfiler</description>
      <RTE_Components_h>
        <!-- the following content goes into file 'RTE_Components.h' -->
        #define RTE_ML_ER_Profiler
      </RTE_Components_h>
      <files>     
        <file category="sourceC" name="src/evtrec_profiler.cc"/>
        <file category="include" name="src/"/>
      </files>
    </component>
  </components>
</package>
