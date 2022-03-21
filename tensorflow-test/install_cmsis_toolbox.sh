sudo rm -rv -f /opt/cbuild
wget https://github.com/Open-CMSIS-Pack/devtools/releases/download/tools%2Ftoolbox%2F0.9.2/cmsis-toolbox.sh
chmod +x ./cmsis-toolbox.sh
./cmsis-toolbox.sh cmsis-toolbox.options
rm cmsis-toolbox.sh
