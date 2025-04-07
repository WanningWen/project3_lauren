#1. Use the `requests` library to download the first 10 webpage results for your search term
#1. Use `bs4` to extract all of the items returned in the search results

#import requests

import argparse
import requests
parser = argparse.ArgumentParser(description= "download items information from EBay into JSON file")

parser.add_argument ('search_term')
args = parser.parse_args ()
print ('args. search_term=', args.search_term)
page_number = 8

# example URLs searching (pillow) https://www.ebay.com/sch/i.html?_nkw=pillow&_sacat=0&_from=R40&_trksid=p4432023.m570.l1313
# example URLs searching (cat) https://www.ebay.com/sch/i.html?_nkw=cat&_sacat=0&_from=R40&_trksid=p4432023.m570.l1313
# starting URL: https://www.ebay.com/sch/i.html?_nkw=
# followed by high+heels&_sacat=0&_from=R40&_trksid=p4432023.m570.l1313
# page 2: https://www.ebay.com/sch/i.html?_nkw=cat&_sacat=0&_from=R40&_pgn=2


for page_number in range (1,11): 
    url = 'https://www.ebay.com/sch/i.html?_nkw='
    url += args.search_term
    url +='&_sacat=0&_from=R40&_pgn='
    url += str(page_number)
    print('url=', url) # ran and prove URL successful

    r = requests.get(url)
    status = r.status_code
    print("status=", status)
    html = r.text
    print ('html=', html [ :50])

