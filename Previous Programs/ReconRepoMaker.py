import os
def createDirectory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def writeFile(filePath, dataContent):
    file = open(filePath, 'w')
    file.write(dataContent)
    file.close()