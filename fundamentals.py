# fundamentals.py

print "Hello World."

title = "Fundamentals"

print "Examples of %s" % title

name = raw_input("Your name: ")

print "Greetings, %s" % name

def defaultGreeting():
    print "A default greeting"

defaultGreeting()

def printMe(me, andMe=""):
    print "%s %s" % (me, andMe)

printMe("this")
printMe("this", "that")
