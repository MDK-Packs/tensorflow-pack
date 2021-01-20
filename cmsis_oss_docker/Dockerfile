FROM ubuntu:latest

#Create internal workspace
WORKDIR /workspace
ADD . /workspace

# Install any needed system packages
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
      build-essential \
      git \
      bzip2 \
      python3 \
      python3-pip \
      curl \
      dos2unix \
      unzip \
      wget && \
    apt-get clean

# Download and unpack arm gcc    
RUN wget -qO- https://developer.arm.com/-/media/Files/downloads/gnu-rm/10-2020q4/gcc-arm-none-eabi-10-2020-q4-major-x86_64-linux.tar.bz2 | tar -xj
ENV PATH "/workspace/gcc-arm-none-eabi-10-2020-q4-major/bin:$PATH"

# Download and install Arm Compiler 6    
RUN wget -qO- https://developer.arm.com/-/media/Files/downloads/compiler/DS500-BN-00026-r5p0-17rel0.tgz | tar xv
RUN ./install_x86_64.sh --i-agree-to-the-contained-eula --no-interactive -d /AC6/
RUN rm ./install_x86_64.sh
ENV PATH "/workspace/gcc-arm-none-eabi-10-2020-q4-major/bin:$PATH"

# Download and install Corestone SSE-300 FVP MPS3
RUN wget -qO- https://developer.arm.com/-/media/Arm%20Developer%20Community/Downloads/OSS/FVP/Corstone-300/FVP_Corstone_SSE-300_Ethos-U55_11.12_57.tgz | tar -xz
RUN ./FVP_Corstone_SSE-300_Ethos-U55.sh --no-interactive --i-agree-to-the-contained-eula -d /workspace/FVP_Corstone_SSE-300_Ethos-U55 
RUN rm ./FVP_Corstone_SSE-300_Ethos-U55.sh
ENV PATH "/workspace/FVP_Corstone_SSE-300_Ethos-U55/models/Linux64_GCC-6.4:$PATH"

# Download and install Corestone SSE-300 FVP MPS2
RUN wget -qO- https://developer.arm.com/-/media/Arm%20Developer%20Community/Downloads/OSS/FVP/Corstone-300/FVP_Corstone_SSE-300_11.10_44.tgz| tar -xz
RUN ./FVP_Corstone_SSE-300.sh --no-interactive --i-agree-to-the-contained-eula -d /workspace/FVP_Corstone_SSE-300
RUN rm ./FVP_Corstone_SSE-300.sh
ENV PATH "/workspace/FVP_Corstone_SSE-300/models/Linux64_GCC-6.4:$PATH"

# Download and install cmsis-build
RUN wget https://github.com/ARM-software/CMSIS_5/releases/download/5.7.0/cbuild_install.0.10.0.sh
RUN chmod +x cbuild_install.0.10.0.sh
RUN ./cbuild_install.0.10.0.sh -x ./cbuild
RUN rm cbuild_install.0.10.0.sh
RUN mv ./cbuild/bin/cbuildgen.lin ./cbuild/bin/cbuildgen
RUN mv GCC.10.2.1.mak ./cbuild/etc/GCC.10.2.1.mak 
ENV PATH "/workspace/cbuild/bin:$PATH"
ENV CMSIS_PACK_ROOT "/workspace/packs"
ENV CMSIS_COMPILER_ROOT "/workspace/cbuild/etc"
ENV CMSIS_BUILD_ROOT "/workspace/cbuild/bin"
RUN cp_init.sh

# Download and install CMSIS-PACK Validation tools
RUN wget https://github.com/ARM-software/CMSIS_5/raw/develop/CMSIS/Utilities/Linux64/PackChk
RUN mkdir /workspace/bin
RUN mv PackChk /workspace/bin/PackChk
RUN chmod +x /workspace/bin/PackChk
ENV PATH "/workspace/bin:$PATH"

# Install Packs: CMSIS, DFP for FVPs 
RUN cp_install.sh packlist


