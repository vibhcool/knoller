import requests
from bs4 import BeautifulSoup
import re


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

def get_links(r_html):
    soup = BeautifulSoup(r_html,'html5lib')
    a_list = soup.find_all('a')
    link_list = []
    for a in a_list:
        #print(a['href'])
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
    url = 'https://www.google.co.in/search?q=' + search_word + '&start='
    # fetching links from 10 google pages i.e. 100 links
    urls = []
    for i in range(10):
        page_url = url + str(i)
        r_html = get_html(page_url)
        url_list = re.findall(r'https?:\/\/[a-z0-9]{0,10}\.?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b[-a-zA-Z0-9@:%_\+.~#?&//=]*', r_html)
        print('hey1', len(url_list))
        url_list = clean_urls(url_list)
        urls = url_list + urls
        print('hey2', len(url_list))
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

