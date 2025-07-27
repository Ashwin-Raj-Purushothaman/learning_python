#Argument
#Pass 3 command line arguments while running the script

from sys import argv


script, First, Second, Third = argv 
print ("The script is called:", script)
print ("Your first variable is:", First)
print ("Your second variable is:", Second)
print ("Your third variable is:", Third)