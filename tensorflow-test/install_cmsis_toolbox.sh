sudo rm -rv -f /opt/cbuild
sudo wget https://github.com/Open-CMSIS-Pack/devtools/releases/download/tools%2Fbuildmgr%2F0.10.5/cbuild_install.sh
sudo chmod +x ./cbuild_install.sh
sudo ./cbuild_install.sh < cmsis-toolbox.options
source /opt/cbuild/etc/setup
