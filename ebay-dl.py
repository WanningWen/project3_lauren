import argparse
import requests
from bs4 import BeautifulSoup
import bs4
import json

'''
price will contain the price of the item in cents, stored as an integer (you should never use floats to store monetary values, because floats can't be represented exactly in computers); if there are multiple prices listed (e.g. $54.99 to $79.99), then you may select either price
status will contain a string stating whether the item is "Brand New", "Refurbished", "Pre-owned", etc.
shipping will contain the price of shipping the item in cents, stored as an integer; if the item has free shipping, then this value should be 0
free_returns will contain a boolean value for whether the item has free returns
items_sold will contain the number of items sold (as an integer)'''

parser = argparse.ArgumentParser(description= "download items information from EBay into JSON file")

parser.add_argument('search_term')
parser.add_argument('--num_pages', default = 10)

args = parser.parse_args ()
print ('args. search_term=', args.search_term)
page_number = 8

items = []

for page_number in range (1,args.num_pages+1): 
    url = 'https://www.ebay.com/sch/i.html?_nkw='
    url += args.search_term
    url +='&_sacat=0&_from=R40&_pgn='
    url += str(page_number)
    print('url=', url) # ran and prove URL successful

    r = requests.get(url)
    status = r.status_code
    print("status=", status)
    html = r.text

    soup = BeautifulSoup (html)
    cards = soup.select('.s-item')
    for card in cards:
        item = {}

        # Name
        title_tag = card.select_one('.s-item__title')
        if title_tag:
            item['name'] = title_tag.get_text(strip=True)
        else:
            continue  # skip if there's no title

        # Price
        price_tag = card.select_one('.s-item__price')
        if price_tag:
            try:
                price_text = price_tag.get_text(strip=True).replace('$', '').replace(',', '')
                if 'to' in price_text:
                    price_text = price_text.split('to')[0].strip()
                price_dollars = float(price_text.replace('US', '').strip('$'))
                item['price'] = int(price_dollars * 100)
            except:
                item['price'] = None

        # Status (Condition)
        status_tag = card.select_one('.SECONDARY_INFO')
        if status_tag:
            item['status'] = status_tag.get_text(strip=True)

        # Shipping
        shipping_tag = card.select_one('.s-item__shipping, .s-item__freeXDays')
        if shipping_tag:
            shipping_text = shipping_tag.get_text(strip=True)
            if 'Free' in shipping_text:
                item['shipping'] = 0
            else:
                try:
                    shipping_text = shipping_text.replace('+$', '').replace('shipping', '').replace(',', '').strip()
                    item['shipping'] = int(float(shipping_text.strip('$')) * 100)
                except:
                    item['shipping'] = None

        # Free returns
        return_tag = card.select_one('.s-item__free-returns')
        item['free_returns'] = return_tag is not None

        # Items sold
        sold_tag = card.select_one('.s-item__hotness, .s-item__additionalItemHotness')
        if sold_tag:
            import re
            match = re.search(r'(\d+(,\d{3})*) sold', sold_tag.get_text())
            if match:
                item['items_sold'] = int(match.group(1).replace(',', ''))

        items.append(item)

    print(items)
    # Save to file
    filename = f"{args.search_term}_items.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(items, f, indent=2, ensure_ascii=False)