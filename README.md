# eBay Item Scraper

This project uses `ebay-dl.py` to download product listings from eBay based on a given search term. It collects information such as item name, price, shipping cost, whether the item offers free returns, and how many units have been sold. The output is saved as a JSON file for each term.

## How to Run

To run the scraper and generate 3 JSON files, use the following commands in your terminal:

```{python}
python3 ebay-dl.py bottle --num_pages 1
python3 ebay-dl.py fragrance --num_pages 1
python3 ebay-dl.py pillow --num_pages 1
```

Each command will download listings for the specified search term (`bottle`, `fragrance`, `pillow`) and save them as `bottle_items.json`, `fragrance_items.json`, and `pillow_items.json`.

## Project Link

You can find the full assignment description here:  
[CSCI040 Project 3 Instructions](https://github.com/mikeizbicki/cmc-csci040/tree/main/projects/03-ebay)

You can find the project repository at:
[My Project 3](Put your link here)