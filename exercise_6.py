#strings and text


x = "There are %d types of people." % 10 #string inside text
binary = "binary" 
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) #string inside text

print (x)
print (y)

print ("I said: %r." % x )#string inside text 
print ("I also said: '%s'." % y) #string inside text

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print (w + e)