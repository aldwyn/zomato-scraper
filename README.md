# Zomato Scraper (Cebu only)

## Output Sample
```json
{
    "rating": "3.7",
    "reviews_count": "11",
    "known_for": "Instagrammable coffee shop and tasting coffee products with its combos",
    "description": "Serves Cafe. Known for Instagrammable coffee shop and tasting coffee products with its combos. Cost Average PHP500 for two people (approx.)",
    "creator": "@zomato",
    "url": "https://www.zomato.com/cebu/32-umber-cafe-co-lahug?ztype=restaurant&zid=18297712&zsource=facebook&fbrefresh=18297712",
    "cuisines": ["Cafe"],
    "longitude": "123.9044220000",
    "id": "18297712",
    "menu_urls": ["https://b.zmtcdn.com/data/menus/712/18297712/6dafa3e86542fbf8d42f56a59b0a4020.jpg", "https://b.zmtcdn.com/data/menus/712/18297712/100d80e939220291acdbc06d40295937.jpg"],
    "address": "The Forum Building, Archbishop Reyes Avenue, Lahug , Cebu City",
    "latitude": "10.3218540000",
    "type": "Caf\u00e9",
    "thumbnail": "https://b.zmtcdn.com/data/pictures/2/18297712/7ef3081abfbe46aec3496e235802ab43_featured_v2.jpg",
    "name": "32 Umber Cafe & Co. - Cebu"
}
```

## Local Installation & Run
```bash
mkvirtualenv zomato-scraper
pip install -r requirements.txt
scrapy crawl restaurants -o restaurants.json
```
