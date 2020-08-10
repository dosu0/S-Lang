#Initilize Vars
lines = []
scanned = []
variables = {}
tokens = ["create", "set", "output"]
separators = [" ", ";", "(", ")", "{","}"]
errors = []
outputs = []
operators = ["+", "*", "/", "-", "**"]

#File Scanner
def ScanFile(filename):
    file = open(filename, "r")
    for line in file:
        lines.append(line)
    file.close()

#Scans Lines
def ScanLine(line):
    scanned.clear()
    string = ""
    for letter in lines[line]:
        if letter in separators:
            if string != "":
                scanned.append(string)
                string = "" 
        else:
            string = string + letter

def ParseLine(line):
    if scanned[0] in tokens:
        if scanned[0] == "create":
            if scanned[1] == "var":
                variables[scanned[2]] = 0
            elif scanned[1] == "list":
                print("Lists are a feauture coming soon")
            else:
                errors.append("Error: Unkown Data Structure/Type " + scanned[1])
        elif scanned[0] == "set":
             variables[scanned[1]] = scanned[3]
        
        elif scanned[0] == "output":
            outputs.append("")
            for word in scanned:
                if word in variables:
                    outputs[len(outputs)-1] = outputs[len(outputs)-1] + str(variables[word])
                elif word in operators:
                    outputs[len(outputs)-1] = outputs[len(outputs)-1] + word
    else:
        errors.append("Error: Unkown token: " + '"' + scanned[0] + '" ' + "on line #" + str(line)) 
## Compile ##
def Compile(fileName):
    ScanFile(fileName)
    print(lines)
    outputs.clear()
    for i in range(len(lines)):
        ScanLine(i)
        ParseLine(i)
    errorlog = open("errorlog.txt", "w")

    for error in errors:
        errorlog.write(error + " \n")
    errorlog.close()
    
    outputlog = open("output.txt", "w")
    print(outputs)
    for output in outputs:
        outputlog.write(str(eval(output)) + "\n")
    outputlog.close()
