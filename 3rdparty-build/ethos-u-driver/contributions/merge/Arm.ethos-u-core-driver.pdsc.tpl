<?xml version="1.0" encoding="UTF-8"?>
<package schemaVersion="1.6" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="PACK.xsd">
  <vendor>Arm</vendor>
  <name>ethos-u-core-driver</name>
  <description>Device Driver for the Arm(R) Ethos(TM)-U NPU.</description>
  <!-- web download link -->
  <url>https://review.mlplatform.org/plugins/gitiles/ml/ethos-u/ethos-u-core-driver/</url>
  <license>LICENSE.txt</license>
  <releases>
    <release version="%{RELEASE_VERSION}%" date="%{RELEASE_DATE}%">
      kissfft for TensorFlow %{RELEASE_VERSION}%
    </release>
  </releases>
  <components>
    <component Cclass="Machine Learning" Cgroup="NPU Support" Csub="Ethos-U Driver" Cvariant="U55" Cversion="1.0.5">
      <description>Driver for Ethos-U55</description>
      <RTE_Components_h>
        <!-- the following content goes into file 'RTE_Components.h' -->
        #define RTE_DataExchange_Math_kissfft     /* kissfft */
      </RTE_Components_h>
      <files>     
        <file category="sourceC" name="ethos_u_core_driver/src/ethosu_device.c"/>
        <file category="sourceC" name="ethos_u_core_driver/src/ethosu_driver.c"/>
        <file category="sourceC" name="ethos_u_core_driver/src/ethosu_pmu.c"/>
        <file category="include" name="ethos_u_core_driver/src/"/>
        <file category="include" name="ethos_u_core_driver/include/"/>
      </files>
    </component>
  </components>
</package>
