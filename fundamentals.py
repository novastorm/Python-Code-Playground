# fundamentals.py

print "Hello World."

aVariableContainer = "a variable"

print "Examples of %s" % aVariableContainer

aName = raw_input("Your name: ")

print "Greetings, %s" % aName

def defaultGreeting():
    print "A default greeting"

defaultGreeting()

def printMe(me, andMe=""):
    print "%s %s" % (me, andMe)

printMe("this")
printMe("this", "that")
