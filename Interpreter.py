import string
lines = []
scannedLine = []
alphnum = string.ascii_letters + string.digits + "_"
#File Scanner
def scan(filename):
    file = open(filename, "r")

    for line in file:

        # Remove the \n character
        scannedLine = line.strip("\n")

        # Convert scannedLine into a list
        scannedLine = scannedLine.split(" ")

        # Add scannedLine to the lines list
        lines.append(scannedLine)

    file.close()


def Parse(line):
    statement(0)

def statement(linenum):
    tok = lines[linenum][0]
    
    if tok == "ID":
        ""

def compile(filename):
    scan(filename)
    statement(0)
    
    


def getTok(word):
    # Operation Check
    if word in ['+', '-', '*', '/', '**']:
        return "oper"

    # Int Check no decimals
    isInt = True
    for letter in word:
        if letter not in string.digits:
            isInt = False
            break
    if isInt == True:
        return "int"

    #string check
    isString = True
    for letter in word:
        if letter not in alphnum:
            isString = False
            break
    if isString == True:
        return "string"