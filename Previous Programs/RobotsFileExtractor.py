import urllib.request
import io

def getRobotsTXT(webURL):
    if url.endswith('/'):
        URLPath = webURL
    else:
        URLPath = webURL + '/'
    
    request = urllib.request.urlopen(URLPath + "robots.txt", dataContent = None)
    dataContent = io.TextIOWrapper(request, encoding="UTF-8")
    return dataContent

print(getRobotsTXT("https://google.com"))