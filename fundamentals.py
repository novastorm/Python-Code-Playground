# fundamentals.py

# output
print "Hello World."

# variable assignment
aVariableContainer = "a variable"

# magic numbers
maxValue = 10

# variable usage
print "Examples of %s" % aVariableContainer

# input from keyboard
aUserName = raw_input("Your name: ")

print "Greetings, %s" % aUserName

# functions with return value
def defaultGreeting():
    return "Greetings"

print defaultGreeting()

# function with parameters and parameter defaults
def printMe(me, andMe=""):
    print "%s %s" % (me, andMe)

printMe("this")
printMe("this", "that")

# function scope and return value
def defaultGreetingFor(aName):
    return "Hello %s, welcome back." % aName

# conditionals

if aUserName == "Adam":
    print defaultGreetingFor(aUserName)
else:
    print defaultGreeting()

# iterators

# while loop
print "while loop"
a = 0
b = 1
value = b
while value < maxValue:
    print value
    value = a + b
    a = b
    b = value

# fast enumeration
print "fast enumeration"
for n in range(maxValue):
    print n

# break, continue, else
