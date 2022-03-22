  #!/bin/sh

find $(pwd) -type f -name "*.pack" > packlist
cat packlist
#sed -i 's/^/file:\/\//' packlist
#cat packlist
cpackget pack add -f packlist -a
cpackget pack add https://www.keil.com/pack/ARM.CMSIS.5.8.0.pack -a
cpackget pack add https://keilpack.azureedge.net/pack/ARM.V2M_MPS3_SSE_300_BSP.1.2.0.pack -a

cd ..
chmod +x install_cmsis_toolbox.sh
./install_cmsis_toolbox.sh
