import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
import re


def crawl_urls(url_list, content_type):
    dict_data = {}
    dict_data['text'] = []
    i = 1
    for url in url_list:
        print('crawling data for', i, 'url', url, '...')
        crawl_url(url, dict_data, 'text')
    return dict_data

def crawl_url(url, dict_data=None, content_type='text'):
    r_html=get_html(url)
    #soup = BeautifulSoup(r_html,'html5lib')
    if content_type in ['text', 'all']:
        data = get_text_data(r_html)
        dict_data['text'] = dict_data['text'] + data
        #print(data)
        #print(len(dict_data['text']))
    #if content_type in ['link', 'all']:
        #data_dict['link'] = get_links(r_html)
    #if content_type in ['image', 'all']:
    #    data_dict['image'] = get_images(soup)
    #if content_type == 'video':
    #    data_dict['video'] = get_videos(soup)

def get_html(url):
    #url = 'https://en.wikipedia.org/wiki/Car'
    try:
        r = requests.get(url)
    except ConnectionError:
        print('Failed to open url.')
    return r.text

# apply Boilerpipe article extractor to improve this. This fails if html is shitty
def get_text_data(r_html):
    data_tokens = r_html.split()
    data_list = []
    data = {}
    start = 0
    html_size = len(data_tokens)
    i = 0
    for start in range(html_size):
        check_head_start = (
                '<h1' in data_tokens[start]
                or '<h2' in data_tokens[start]
                or '<h3' in data_tokens[start]
                or '<h4' in data_tokens[start]
                or '<h5' in data_tokens[start]
                or '<h6' in data_tokens[start]
        )
        if check_head_start:
            i = start
            if 'head' in data:
                data_list.append(data)
                data = {}
            check_head_end = (
                    '</h1>' in data_tokens[i]
                    or '</h2>' in data_tokens[i]
                    or '</h3>' in data_tokens[i]
                    or '</h4>' in data_tokens[i]
                    or '</h5>' in data_tokens[i]
                    or '</h6>' in data_tokens[i]
            )
            while not check_head_end:
                i += 1
                if i >= len(data_tokens):
                    break
                check_head_end = (
                    '</h1>' in data_tokens[i]
                    or '</h2>' in data_tokens[i]
                    or '</h3>' in data_tokens[i]
                    or '</h4>' in data_tokens[i]
                    or '</h5>' in data_tokens[i]
                    or '</h6>' in data_tokens[i]
                )
            data['head'] = get_clean_data(' '.join(data_tokens[start:i+1]))
            start = i

        if i >= len(data_tokens):
            break

        if '<p ' in data_tokens[start] or '<p>' in data_tokens[start]:
            i = start
            if 'para' not in data:
                data['para'] = []
            while '</p>' not in data_tokens[i]:
                i += 1
                if i >= len(data_tokens):
                    break
            data['para'].append(get_clean_data(' '.join(data_tokens[start:i+1])))
            
            start = i
        start += 1
    if 'head' in data:
        data_list.append(data)
    return data_list

def get_clean_data(data):
    data = re.sub(r'<[^>]*>', '', data)
    return data

def get_links(r_html, url=None):
    if url != None:
        print('hey')
    link_list = re.findall(r'(https?:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b[-a-zA-Z0-9@:%_\+.~#?&//=]*', r_html)
    return link_list

def get_images(r_html):
    a_list = soup.findAll('img')
    link_list = []
    for a in a_list:
        #print(a['src'])
        link_list.append(a['src'])
    return link_list

#TODO: Code this (not imp right now)
def get_videos(soup):
    pass

def get_urls(search_word):
    url = 'https://www.google.co.in/search?q=' + search_word + '&start='
    # fetching links from 10 google pages i.e. 100 links
    urls = []
    for i in range(10):
        page_url = url + str(i)
        r_html = get_html(page_url)
        url_list = re.findall(r'https?:\/\/[a-z0-9]{0,10}\.?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b[-a-zA-Z0-9@:%_\+.~#?&//=]*', r_html)
        #print('hey1', len(url_list))
        url_list = clean_urls(url_list)
        urls = url_list + urls
        #print('hey2', len(url_list))
        #url_list = clean_urls(url_list)
    #print(len(urls))
    return urls

def clean_urls(url_list):
    k_urls = []
    for url in url_list:
        if url_correct(url):
            k_urls.append(url)
    return k_urls

def url_correct(url):
    if url == None:
        return False
    if 'www.google.co' in url:
        return False
    #if '/url?q=' = url[:7]:
    #    return False
    return True

