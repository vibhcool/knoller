from lib import scrape_data
from lib import refine_data

# Main method
def extract_data(search_word, related_word=None, content_type=None):
    print('starts extraction...')
    if related_word == None:
        related_word = ''
    if content_type == None:
        content_type = ''
    url_list = fetch_urls_list(search_word, related_word)
    print('done url extraction, extracted best', len(url_list), 'urls...')
    data_dict = fetch_data(url_list, content_type, related_word)
    #output_data(data_dict)
    return data_dict

def fetch_urls_list(search_word, related_word=None):
    # At present we crawl google, get all links and choose top 5 results,
    # later, we can improve
    print('starts url extraction...')
    return get_top_urls(search_word, related_word)

def fetch_data(url_list, content_type, related_word):
    print('starts scraping data...')
    data_list = scrape_data.crawl_urls(url_list, content_type)
    #imp_data = select_imp_data(data_list, related_word)
    return data_list

def output_data(data_dict):
    #TODO: code this method, output shall have images, text(text, reference
    # links, imp words from text), links, 
    print(data_dict)

def get_top_urls(search_word, related_word):
    url_list = scrape_data.get_urls(search_word)
    best_urls = refine_data.refine_urls(url_list, related_word)
    return best_urls
