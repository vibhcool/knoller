import scrape_data
import refine_data

# Main method
def extract_data(search_word, related_word=None, content_type=None):
    url_list = fetch_urls_list(search_word)
    data_dict = fetch_data(url_list, content_type, related_word)
    output_data(data_dict)

def fetch_urls_list(search_word):
    # At present we crawl google, get all links and choose top 5 results,
    # later, we can improve
    return get_top_urls(search_word, related_word)

def fetch_data(url_list, content_type, related_word):
    data_list = crawl_urls(url_list, content_type)
    imp_data = select_imp_data(data_list, related_word)
    return imp_data

def output_data(data_dict):
    #TODO: code this method, output shall have images, text(text, reference
    # links, imp words from text), links, 
    print(data_dict)

def get_top_urls(search_word, related_word):
    url_list = get_urls(search_word)
    best_urls = refine_urls(url_list, related_word)
    return best_urls
