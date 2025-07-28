formatter = "%r %r %r %r"

#if there is not 4 arguments in this, it throws error "TypeError: not enough arguments for format string"
print (formatter % (1,2,3,4))
print (formatter % ("one","two","three", "four")) 
print (formatter % (True, False, False, True))
print (formatter % (formatter,formatter,formatter,formatter)) #prints the %r inside the variable formatter
print (formatter % ("hello", "there", "how are", "you?"))
