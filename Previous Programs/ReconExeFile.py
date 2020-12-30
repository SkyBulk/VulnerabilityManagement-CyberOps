from ReconRepoMaker import *
from TopLevelDomainExtractor import *
from IPAddressGrabber import *
from NMAPBasic import *
from RobotsFileExtractor import *
from WhoIs import *

ROOT_DIR = "Corporates"
createDirectory(ROOT_DIR)

def gatherInfo(companyName, webURL):
    robotsText = getRobotsTXT(webURL)
    domain = domainName(webURL)
    IPAddress = getIPAddress(domain)
    NMAP = getNMAP('-F', IPAddress)
    whoIS = getWhois(domain)

    createReport(companyName, webURL, domain, NMAP, robotsText, whoIS)

def createReport(companyName, webURL, domain, NMAP, robotsText, whoIS):
    projectDirectory = ROOT_DIR + "/" + companyName
    createDirectory(projectDirectory)

    writeToFile(projectDirectory + "/URL.txt", webURL)
    writeToFile(projectDirectory + "/DomainName.txt", domain)
    writeToFile(projectDirectory + "/NMAPResult.txt", NMAP)
    writeToFile(projectDirectory + "/RobotsText.txt", robotsText)
    writeToFile(projectDirectory + "/WhoISResult.txt", whoIS)

gatherInfo('Google', 'https://www.google.com')