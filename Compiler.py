import tkinter as tk
import tkinter.font as font
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
            else:
                errors.append("Error: Unkown Object " + scanned[1])
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
def compile():
    ScanFile("Code.txt")
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

    for output in outputs:
        outputlog.write(str(eval(output)) + "\n")
    outputlog.close()


#Start of Main
compile()

#Window Script
window = tk.Tk(className="s-lang hub")

titleFont = font.Font(size=30)
title = tk.Label(
    text="Welcome to S-lang"
)
title['font'] = titleFont


description = tk.Label(
    text="S-lang is a simple programming language"
)

entry = tk.Entry(
)
fileName = entry.get()

compilebutton = tk.Button(
    text="Compile"
)
textBox = tk.Text()
description.pack()
compilebutton.pack()
entry.pack()
textBox.pack()

print(fileName)
window.mainloop()
window.destroy()


