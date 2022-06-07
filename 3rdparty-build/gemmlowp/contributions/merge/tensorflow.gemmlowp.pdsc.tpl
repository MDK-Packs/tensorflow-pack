<?xml version="1.0" encoding="UTF-8"?>
<package schemaVersion="1.6" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="PACK.xsd">
  <vendor>tensorflow</vendor>
  <name>gemmlowp</name>
  <description>a small self-contained low-precision GEMM library</description>
  <!-- web download link -->
  <url>https://github.com/MDK-Packs/tensorflow-pack/releases/download/%{RELEASE_VERSION}%/</url>
  <license>LICENSE.txt</license>
  <releases>
    <release version="%{RELEASE_VERSION}%" date="%{RELEASE_DATE}%">
      gemmlowp for TensorFlow %{RELEASE_VERSION}%
    </release>
    %{HISTORY}%
  </releases>
  <taxonomy>
    <description Cclass="Data Processing">Software Components for Data Processing</description>
    <description Cclass="Data Processing" Cgroup="Math">Math Components</description>
  </taxonomy>
  <components>
    <component Cclass="Data Processing" Cgroup="Math" Csub="gemmlowp fixed-point" Cvariant="tensorflow" Cversion="%{RELEASE_VERSION}%">
      <description>Jsmn</description>
      <RTE_Components_h>
        <!-- the following content goes into file 'RTE_Components.h' -->
        #define RTE_DataExchange_Math_gemmlowp     /* gemmlowp */
      </RTE_Components_h>
      <files>
        <file category="include" name="src/"/>
      </files>
    </component>
  </components>
</package>
