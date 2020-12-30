import os
def getWhois(webURL):
    commandInput = "whois " + webURL
    processCreate = os.popen(commandInput)
    convertResultString = str(processCreate.read())
    return convertResultString

print(getWhois('google.com'))