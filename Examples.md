# Example Snippets

## Run scraping of program
```
from lib import scrape_data
data = scrape_data.crawl_urls(['https://en.wikipedia.org/wiki/RDFa'], 'all')
print(data['text'])
```

## Run complete program
```
from lib import main_file
data = main_file.extract_data('car')
print(data['text'])
```
