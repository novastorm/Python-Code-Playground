# input-output.py

# review console I/O
# CLI parameters
# file I/O

# input from keyboard
def getUserName():
    aName = raw_input("Your name: ")
    return aName

def printGreeting(aName):
    print "Greetings, %s" % aName

userName = getUserName()
printGreeting(userName)
