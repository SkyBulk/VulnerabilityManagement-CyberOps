# host 'TOPLEVELDOMAIN'

def getIPAddress(webURL):
    commandInput = "host " + webURL
    processCreate = os.popen(commandInput)
    convertResultString = str(process.read())
    markPoint = convertResultString.find("has address") + 12
    return convertResultString[markPoint:].splitlines()[0]

print(getIPAddress("google.com"))
