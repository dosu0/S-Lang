import string
lines = []
scannedLine = []

#Test


#File Scanner
def ScanFile(filename):
    file = open(filename, "r")

    for line in file:

        # Remove the \n character
        scannedLine = line.strip("\n")

        # Convert scannedLine into a list
        scannedLine = scannedLine.split(" ")

        # Add scannedLine to the lines list
        lines.append(scannedLine)

    file.close()


def scanLine(line):
    scanned = []
    for word in line:
        scanned.append(getType(word))
    return scanned


def compile(filename):
    ScanFile(filename)
    for line in lines:
        print(scanLine(line))


def getType(word):
    # Operation Check
    if word in ['+', '-', '*', '/', '**']:
        return "oper"

    # Int Check no decimals
    isInt = True
    isDecimal = False
    for letter in word:
        if letter not in string.digits:
            isInt = False
            break
    if isInt == True:
        return "int"

    #string check
    isString = True
    for letter in word:
        if letter not in string.ascii_letters:
            isString = False
            break
    if isString == True:
        return "string"
