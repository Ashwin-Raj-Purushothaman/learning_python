from sys import argv

script, filename =argv

txt = open(filename) # open() open the file and passing it to variable txt 

print ("Heres Your File %r:" %filename) #strong to the text
print (txt.read()) # read() - read the file. txt. passes the file to read()

print ("Type the filename again:")
file_again = input(">") #prompt input, saving the file name in file_again

txt_again = open(file_again) #file_again passes the filename to the open() and saved in txt_again

print (txt_again.read()) #txt_again. passes the opened file to read()

