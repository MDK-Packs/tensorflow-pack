#!/bin/sh

find $(pwd) -type f -name "*.pack" > packlist
cat packlist
sed -i 's/^/file:\/\//' packlist
cat packlist
cp_install.sh packlist
