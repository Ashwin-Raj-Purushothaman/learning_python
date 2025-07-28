#Names, Variables, Code, Functions

#scripts with argv

#def function -> Define, * -> tells python to take all the arguments to the function and put them in args (*args) as list.
def print_two(*args): # line ends with :
	arg1, arg2 = args
	print ("arg1: %r, arg2: %r" %(arg1,arg2))

def print_two_again(arg1, arg2):
	print ("arg1 %r, arg2 %r" % (arg1, arg2))
	
#one argument 

def print_one(arg1):
	print ("arg1 %r" % arg1)
	
#no argument

def print_none():
	print("Nothing inside")
	
print_two("Ash", "Win")
print_two_again("Man","Mann")
print_one ("1st!!")
print_none()


