import os

def getNMAP(attributes, IP):
    commandInput = "nmap " + attributes + " " + IP
    processCreate = os.popen(commandInput)
    convertResultString = str(processCreate.read())
    return convertResultString

print(getNMAP('-F', '200.100.50.25'))