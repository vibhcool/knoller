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

a = ['https://droom.in/car&sa=U&ved=0ahUKEwi1vcGanpjXAhXMOY8KHaDJBiw4CRAWCBMwAA&usg=AOvVaw0UthIA_PjfeiJ_KiN9x2tx', 'http://webcache.googleusercontent.com/search%3Fq%3Dcache:tB3dO09QevAJ:https://droom.in/car%252Bcar%26hl%3Den%26ct%3Dclnk&sa=U&ved=0ahUKEwi1vcGanpjXAhXMOY8KHaDJBiw4CRAgCBYwAA&usg=AOvVaw1PLIXOaFHkukH2NZ-fOkHo', 'https://volercars.com/delhi&sa=U&ved=0ahUKEwi1vcGanpjXAhXMOY8KHaDJBiw4CRAWCBkwAQ&usg=AOvVaw2Y3uKTrYZP0GOMoA5G7iNG', 'http://webcache.googleusercontent.com/search%3Fq%3Dcache:JJ7pmo96YXkJ:https://volercars.com/delhi%252Bcar%26hl%3Den%26ct%3Dclnk&sa=U&ved=0ahUKEwi1vcGanpjXAhXMOY8KHaDJBiw4CRAgCBwwAQ&usg=AOvVaw2ijM1qwxKuU-b6v7mNnMiN', 'https://www.cardekho.com/latestcars&sa=U&ved=0ahUKEwi1vcGanpjXAhXMOY8KHaDJBiw4CRAWCB4wAg&usg=AOvVaw0sBw_HzRccw65dFuwBZeHr', 'http://webcache.googleusercontent.com/search%3Fq%3Dcache:fx4ZoKH4amAJ:https://www.cardekho.com/latestcars%252Bcar%26hl%3Den%26ct%3Dclnk&sa=U&ved=0ahUKEwi1vcGanpjXAhXMOY8KHaDJBiw4CRAgCCEwAg&usg=AOvVaw0rbsuw9Efk7jcP9CYDVN52', 'https://www.marutisuzukitruevalue.com/buy-car&sa=U&ved=0ahUKEwi1vcGanpjXAhXMOY8KHaDJBiw4CRAWCCMwAw&usg=AOvVaw0jnRyJHPsT0au-SWiCfg7X', 'http://webcache.googleusercontent.com/search%3Fq%3Dcache:9u_9JRsQ7EMJ:https://www.marutisuzukitruevalue.com/buy-car%252Bcar%26hl%3Den%26ct%3Dclnk&sa=U&ved=0ahUKEwi1vcGanpjXAhXMOY8KHaDJBiw4CRAgCCYwAw&usg=AOvVaw3LFCXYRFz6WplmiYqYnmE1', 'https://www.cartrade.com/new-cars&sa=U&ved=0ahUKEwi1vcGanpjXAhXMOY8KHaDJBiw4CRAWCCgwBA&usg=AOvVaw2R9kswhf-hf1ra74ziY4u3', 'http://webcache.googleusercontent.com/search%3Fq%3Dcache:aI6PzNmkRFgJ:https://www.cartrade.com/new-cars%252Bcar%26hl%3Den%26ct%3Dclnk&sa=U&ved=0ahUKEw$1vcGanpjXAhXMOY8KHaDJBiw4CRAgCCswBA&usg=AOvVaw1_-beSlS5k_3FgEFtYGXRR', 'https://www.autocarindia.com/news&sa=U&ved=0ahUKEwi1vcGanpjXAhXMOY8KHaDJBiw4C$AWCC0wBQ&usg=AOvVaw2A_qmWPQHYmrRCjR6kJEVy', 'http://webcache.googleusercontent.com/search%3Fq%3Dcache:RsjoFWBmCFYJ:https://www.autocarindia.com/news%$52Bcar%26hl%3Den%26ct%3Dclnk&sa=U&ved=0ahUKEwi1vcGanpjXAhXMOY8KHaDJBiw4CRAgCDAwBQ&usg=AOvVaw3dR3UL4Ye73FheuOZwgfmn', 'https://www.hondacarindia.com/c$r-dealers-showrooms&sa=U&ved=0ahUKEwi1vcGanpjXAhXMOY8KHaDJBiw4CRAWCDMwBg&usg=AOvVaw3eWX9E6PDpDtLxjaNyabj0', 'http://webcache.googleusercontent.com/se$rch%3Fq%3Dcache:wRYWKJYqJdwJ:https://www.hondacarindia.com/car-dealers-showrooms%252Bcar%26hl%3Den%26ct%3Dclnk&sa=U&ved=0ahUKEwi1vcGanpjXAhXMOY8KHaDJ$iw4CRAgCDYwBg&usg=AOvVaw35kG0Tio6-0Lb_SBCsFVym', 'https://www.youtube.com/watch%3Fv%3DjCPR6a30h0I&sa=U&ved=0ahUKEwi1vcGanpjXAhXMOY8KHaDJBiw4CRC3Agg5M$c&usg=AOvVaw06TkyxKkWZTU6npan_sko3', 'https://www.youtube.com/watch%3Fv%3DjCPR6a30h0I&sa=U&ved=0ahUKEwi1vcGanpjXAhXMOY8KHaDJBiw4CRC4Agg6MAdQAQ&usg=AO$Vaw0q3gS7TmKF6hZMs_FORrd5', 'https://en.wikipedia.org/wiki/Car&sa=U&ved=0ahUKEwi1vcGanpjXAhXMOY8KHaDJBiw4CRAWCDwwCA&usg=AOvVaw3GmadGz0581xajkXg1POnI', 'http://webcache.googleusercontent.com/search%3Fq%3Dcache:mbNbG1lcjhkJ:https://en.wikipedia.org/wiki/Car%252Bcar%26hl%3Den%26ct%3Dclnk&sa=U&ved=0ahU$Ewi1vcGanpjXAhXMOY8KHaDJBiw4CRAgCD8wCA&usg=AOvVaw3bnKflp-gp2vskFNLlkjHt', 'http://www.businesstoday.in/photos/in-the-news/top-10-cars-under-5-lakhs-a$to-800-k10-swift-tiago-kwid-grand-i10-wagon-r-figo/1105.html&sa=U&ved=0ahUKEwi1vcGanpjXAhXMOY8KHaDJBiw4CRAWCEIwCQ&usg=AOvVaw3iLut_IG1x3BEZLFZK-KHa', 'http://webcache.googleusercontent.com/search%3Fq%3Dcache:1qhfKxSuMxgJ:http://www.businesstoday.in/photos/in-the-news/top-10-cars-under-5-lakhs-alto-80-k10-swift-tiago-kwid-grand-i10-wagon-r-figo/1105.html%252Bcar%26hl%3Den%26ct%3Dclnk&sa=U&ved=0ahUKEwi1vcGanpjXAhXMOY8KHaDJBiw4CRAgCEUwCQ&usg=AOvVaw$gqc3E4xR_W1D1fiHQFn9Q']
