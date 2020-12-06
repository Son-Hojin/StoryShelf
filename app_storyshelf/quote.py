from selenium import webdriver
from bs4 import BeautifulSoup
import random

quote_list = []
author_list = []

saying_list = []

def find_viewlist():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    #options.add_argument('window-size=1920x1080')
    chrome_options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu") # 위 코드에서 오류가 나면 대시(-) 두 개 붙이기

    driver = webdriver.Chrome('app_storyshelf/driver/chromedriver.exe', options=chrome_options)
    
    driver.get("http://naver.com")

    elem_query = driver.find_element_by_id("query")
    elem_query.clear()
    elem_query.send_keys("독서 명언")
    print("명언 가져오는중", end="")
    xpath = '//*[@id="search_btn"]'
    driver.find_element_by_xpath(xpath).click()
    
    print('.', end="")
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    viewlist = soup.findAll("div", {'class': 'viewlst'})
    print('.')
    return viewlist

def extract_quote(viewlist):
    quote_list.clear()
    for view in viewlist:
        quote_list.append(view.find('p',{'class':"lngkr"}).text)

def extract_author(viewlist):
    author_list.clear()
    for view in viewlist:
        author_list.append(view.find('dl').find('a',{'nocr':''}).text)


def print_quote():
    #for i in range(len(author_list)):
    for quote, author in zip(quote_list,author_list):
        print('"',end='')
        print(quote, end='')
        print('"')
        print("\t- ", end="")
        print(author, end=" -\n")

def random_quote():
    rand_num = random.randrange(0,len(quote_list))
    print('"'+quote_list[rand_num]+'"')
    print('-'+author_list[rand_num])

def make_list():
    viewlist = find_viewlist()
    extract_quote(viewlist)
    extract_author(viewlist)
    for quote, author in zip(quote_list, author_list):
        temp_dict = dict(saying=quote, author=author)
        saying_list.append(temp_dict)

    return saying_list


#viewlist = find_viewlist()
#extract_quote(viewlist)
#extract_author(viewlist)
#random_quote()


