<?xml version="1.0" encoding="UTF-8"?>
<package schemaVersion="1.6" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="PACK.xsd">
  <vendor>tensorflow</vendor>
  <name>flatbuffers</name>
  <description>FlatBuffers: Memory Efficient Serialization Library</description>
  <!-- web download link -->
  <url>https://github.com/MDK-Packs/tensorflow-pack/releases/download/0.4/</url>
  <license>LICENSE.txt</license>
  <releases>
    <release version="%{RELEASE_VERSION}%" date="%{RELEASE_DATE}%">
      Flatbuffers for TensorFlow %{RELEASE_VERSION}%
    </release>
  </releases>
  <taxonomy>
    <description Cclass="Data Exchange">Software Components for Data Exchange</description>
    <description Cclass="Data Exchange" Cgroup="Serialization">Data Serializer Components</description>
  </taxonomy>
  <components>
    <component Cclass="Data Exchange" Cgroup="Serialization" Csub="flatbuffers" Cvariant="tensorflow" Cversion="1.12.0">
      <description>Flatbuffers</description>
      <RTE_Components_h>
        <!-- the following content goes into file 'RTE_Components.h' -->
        #define RTE_DataExchange_Serialization_flatbuffers     /* flatbuffers */
      </RTE_Components_h>
      <files>
        <file category="include" name="src/include/"/>
      </files>
    </component>
  </components>
</package>
