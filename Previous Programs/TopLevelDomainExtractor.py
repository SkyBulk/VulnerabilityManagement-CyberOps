from tld import get_tld

# Install 'tld' : sudo pip3 install tld
# whois 'TOPLEVELDOMAIN'

def topLevelDomain(webURL):
    domainName = get_tld(webURL)
    return domainName

print(topLevelDomain('https://google.com'))
