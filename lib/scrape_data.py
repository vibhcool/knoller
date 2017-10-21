import requests
from bs4 import BeautifulSoup


def crawl_urls(url_list, content_type):
    dict_list = []
    for url in url_list:
        dict_list.append(crawl_url(url, content_type))

def crawl_url(url, content_type='text'):

    r_html=get_html(url)
    soup = BeautifulSoup(r_html,'html5lib')
    data_dict = {}
    if content_type in ['text', 'all']:
        data_dict['text'] = get_text(soup)
    if content_type in ['link', 'all']:
        data_dict['link'] = get_links(soup)
    if content_type in ['image', 'all']:
        data_dict['image'] = get_images(soup)
    if content_type == 'video':
        data_dict['video'] = get_videos(soup)
    return data_dict

def get_html(url):
    #url = 'https://en.wikipedia.org/wiki/Car'
    r = requests.get(url)
    return r.text

# apply Boilerpipe article extractor to improve this
def get_text(soup):
    para_list = soup.findAll('p', text=True)
    text_list = []
    for para in para_list:
        print(para)
        text_list.append(para)
    return text_list

def get_links(soup):
    a_list = soup.findAll('a')
    link_list = []
    for a in a_list:
        print(a['href'])
        link_list.append(a['href'])
    return link_list


def get_images(soup):
    a_list = soup.findAll('img')
    link_list = []
    for a in a_list:
        print(a['src'])
        link_list.append(a['src'])
    return link_list

#TODO: Code this (not imp right now)
def get_videos(soup):
    pass

def get_urls(search_word):
    url = 'https://www.google.co.in/search?q=car&start='
    # fetching links from 10 google pages i.e. 100 links
    for i in range(10):
        page_url = url + str(i) + '0'
        r_html=get_html(page_url)
        soup = BeautifulSoup(r_html,'html5lib')
        url_list = get_links(soup)
        for i in range(0, len(url_list)):
            if not url_correct(url_list[i]):
                url_list.pop(i)
            #else:
            #    url_list[i] = fetch_url(url)
    return url_list

def url_correct(url):
    if url == None:
        return False
    if url.find('www.google.co') == -1:
        return False
    #if url.find('/url?sa=') == -1:
    #    return False
    return True

# If url isn't fetched properly
def fetch_url(url):
    return url[url.index('/url?sa=') + len('/url?sa='):]
