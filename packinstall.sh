#!/bin/sh

find $(pwd) -type f -name "*.pack" > packlist
sed -i '1s/^/file:\/\//' packlist
cp_install.sh packlist
