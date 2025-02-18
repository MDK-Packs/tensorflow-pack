<?xml version="1.0" encoding="UTF-8"?>
<package schemaVersion="1.6" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="PACK.xsd">
  <vendor>tensorflow</vendor>
  <name>kissfft</name>
  <description>Fast Fourier Transform (FFT) library that tries to Keep it Simple, Stupid</description>
  <!-- web download link -->
  <url>https://github.com/MDK-Packs/tensorflow-pack/releases/download/%{RELEASE_VERSION}%/</url>
  <license>LICENSE.txt</license>
  <releases>
    <release version="%{RELEASE_VERSION}%" date="%{RELEASE_DATE}%">
      kissfft for TensorFlow %{RELEASE_VERSION}%
    </release>
    %{HISTORY}%
  </releases>
  <components>
    <component Cclass="Data Processing" Cgroup="Math" Csub="kissfft" Cvariant="tensorflow" Cversion="%{RELEASE_VERSION}%" isDefaultVariant="true" >
      <description>KISS FFT</description>
      <RTE_Components_h>
        <!-- the following content goes into file 'RTE_Components.h' -->
        #define RTE_DataExchange_Math_kissfft     /* kissfft */
      </RTE_Components_h>
      <files>     
        <file category="sourceC" name="src/kiss_fft.c"/>
        <file category="sourceC" name="src/tools/kiss_fftr.c"/>
        <file category="include" name="src/"/>
        <file category="include" name="src/tools/"/>
      </files>
    </component>
  </components>
</package>
