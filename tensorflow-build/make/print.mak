
# Print internal variables (used by CMSIS-Pack build)
printvar-%: 
	@echo '$*=$($*)'

# Print variable with enclosing tags (used by CMSIS-Pack build)
printvar-tagged-%: 
	@echo '$*=<LIST>$($*)</LIST>'

