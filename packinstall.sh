#!/bin/sh

find $(pwd) -type f -name "*.pack" > packlist
cat packlist
sed -i '1s/^/file:\/\//' packlist
cat packlist
cp_install.sh packlist
