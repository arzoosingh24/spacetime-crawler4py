import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def scraper(url, resp):
    links = extract_next_links(url, resp)
    
    # gets rid of fragment part of URL
    defragmented = []
    for link in links:
        parsed = urlparse(link)
        defragmented.append(parsed.scheme + netloc + path + params + query)

    return [link for link in links if is_valid(link)]

def extract_next_links(url, resp):
    parsed = urlparse(url)
    finalLinks = []
    # Implementation required.
    # url: the URL that was used to get the page
    # resp.url: the actual url of the page
    # resp.status: the status code returned by the server. 200 is OK, you got the page. Other numbers mean that there was some kind of problem.
    # resp.error: when status is not 200, you can check the error here, if needed.
    # resp.raw_response: this is where the page actually is. More specifically, the raw_response has two parts:
    #         resp.raw_response.url: the url, again
    #         resp.raw_response.content: the content of the page!
    # Return a list with the hyperlinks (as strings) scrapped from resp.raw_response.content
    return list()

def checkNetLoc(netloc, path):
    if "ics.uci.edu" not in netloc and "cs.uci.edu" not in netloc and "informatics.uci.edu" not in netloc and "stat.uci.edu" not in netloc and "today.uci.edu" not in netloc:
        return False # make sure that the netlocation is one of the ics sites
    if "today.uci.edu" in netloc and "/department/information_computer_sciences" not in path:
        return False # if the today.uci.edu doesnt have "/department/information_computer_sciences" in it 
    if "archive.ics.uci.edu" in netloc or "grape.ics.uci.edu" in netloc or "intranet.ics.uci.edu" in netloc:
        return False # we can't have archive or grape or intranet on there
    if "wics.ics.uci.edu" in netloc and ("events" in path or "contact" in path):
        return False
    if "hack.ics.uci.edu" in netloc and "contact" in path:
        return False
    return True


def is_valid(url):
    # Decide whether to crawl this url or not. 
    # If you decide to crawl it, return True; otherwise return False.
    # There are already some conditions that return False.
    try:
        parsed = urlparse(url)
        
        if parsed.scheme != "http" and parsed.scheme != "https":
            return False

        if checkNetLoc(parsed.netloc, parsed.path) == False:
            return False
        
        
        return not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise
