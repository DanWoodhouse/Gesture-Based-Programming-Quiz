firstName = ""
lastName = ""

def getName():
    global firstName
    firstName = "John"

    global lastName
    lastName = "Smith"

getName()

print (firstName, lastName)
