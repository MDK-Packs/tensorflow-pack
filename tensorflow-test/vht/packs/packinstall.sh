  #!/bin/sh

find $(pwd) -type f -name "*.pack" > packlist
cat packlist
#sed -i 's/^/file:\/\//' packlist
#cat packlist
cpackget pack add -f packlist -a
