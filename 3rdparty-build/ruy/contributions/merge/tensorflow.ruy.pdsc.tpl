<?xml version="1.0" encoding="UTF-8"?>
<package schemaVersion="1.6" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="PACK.xsd">
  <vendor>tensorflow</vendor>
  <name>ruy</name>
  <description>The ruy matrix multiplication library</description>
  <!-- web download link -->
  <url>https://github.com/MDK-Packs/Pack/raw/master/TensorFlow-Pack/</url>
  <license>LICENSE.txt</license>
  <releases>
    <release version="%{RELEASE_VERSION}%" date="%{RELEASE_DATE}%">
      ruy for TensorFlow %{RELEASE_VERSION}%
    </release>
  </releases>
  <taxonomy>
    <description Cclass="Data Processing">Software Components for Data Processing</description>
    <description Cclass="Data Processing" Cgroup="Math">Math Components</description>
  </taxonomy>
  <components>
    <component Cclass="Data Processing" Cgroup="Math" Csub="ruy" Cvariant="tensorflow" Cversion="%{RELEASE_VERSION}%">
      <description>Flatbuffers</description>
      <RTE_Components_h>
        <!-- the following content goes into file 'RTE_Components.h' -->
        #define RTE_DataProcessing_Math_ruy     /* ruy */
      </RTE_Components_h>
      <files>
        <file category="include" name="src/"/>
      </files>
    </component>
  </components>
</package>
