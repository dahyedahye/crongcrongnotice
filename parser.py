import os
## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KrongCrawl.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

from selenium import webdriver

from bs4 import BeautifulSoup
import time
from KrongKrongCrawl.models import CauData
from KrongKrongCrawl.models import ElectricData
from KrongKrongCrawl.models import SocialData
from KrongKrongCrawl.models import BisData
from KrongKrongCrawl.models import CmpengData




def parse_cau():
    from selenium import webdriver
    from bs4 import BeautifulSoup
    import time

        ## setup Driver|Chrome : 크롬드라이버를 사용하는 driver 생성
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
        # 혹은 options.add_argument("--disable-gpu")


    driver = webdriver.Chrome(r'C:\Users\Dabui\Desktop\practice\chromedriver_win32\chromedriver.exe', chrome_options=options)
    driver.implicitly_wait(3)  ## 암묵적으로 웹 자원을 (최대) 3초 기다리기
    ## Login
    driver.get('https://www.cau.ac.kr/04_ulife/causquare/notice/notice_list.php?bbsId=cau_notice') #중앙대학교 메인 홈페이지 공지사항 페이지 불러오기

    time.sleep(3) #html 전체를 제대로 불러오기 위해 3초간 기다립니다

    html = driver.page_source #불러온 페이지의 html 소스들을 html이라는 변수에 할당


    soup = BeautifulSoup(html, 'html.parser')

    driver.get('http://localhost:8000/')
    time.sleep(1)
    html_crong = driver.page_source
    soup_crong = BeautifulSoup(html_crong, 'html.parser')
    crong_line = soup_crong.findAll('a')


    crong_item = []



    for line in crong_line:
        crong_item.append(line.text)

    # print(crong_item)
    # print(type(crong_item))
    #     crong_item = bis_line[0].text


    cau_item_dict = {}
    cau_first_link = 'https://www.cau.ac.kr/04_ulife/causquare/notice/notice_view.php?primaryNum='  # 게시물 뷰 링크의 앞부분을 변수에 할당
    cau_last_link = '&bbsId=cau_notice&schKey=title&schVal=&category1=&timestamp=1514950811572&page=1&pageSize=30'  # 게시물 뷰 링크의 뒷부분을 변수에 할당
    cau_row = soup.findAll('td', {"class": "subject"})


    for items in cau_row:
        cau_line = items.select('a')
        cau_item = cau_line[0].text
        if cau_item not in crong_item:
            cau_link_str = str(cau_line)
            cau_num_link = cau_link_str[28:33]
            cau_item_link = cau_first_link + cau_num_link + cau_last_link  # 링크 생성. 이렇게 변수로 이어준 이유는, 다닥다닥 concatination하기 위해서는 '+' 사용해 이어줘야하고, '+'로 연결하려면 type이 같아야 하기 때문임.
            cau_item_dict[cau_item] = cau_item_link
    return cau_item_dict
    #  print(item_link) #링크 프린트


def parse_electric():
    ## setup Driver|Chrome : 크롬드라이버를 사용하는 driver 생성
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")


    driver = webdriver.Chrome(r'C:\Users\Dabui\Desktop\practice\chromedriver_win32\chromedriver.exe', chrome_options=options)
    driver.implicitly_wait(3)  ## 암묵적으로 웹 자원을 (최대) 3초 기다리기
    ## Login
    driver.get('http://e3home.cau.ac.kr/20141201/sub08/sub01.php')  # 중앙대학교 메인 홈페이지 공지사항 페이지 불러오기

    time.sleep(3)  # html 전체를 제대로 불러오기 위해 3초간 기다립니다

    html = driver.page_source  # 불러온 페이지의 html 소스들을 html이라는 변수에 할당

    soup = BeautifulSoup(html, 'html.parser')

    driver.get('http://localhost:8000/')
    time.sleep(1)
    html_crong = driver.page_source
    soup_crong = BeautifulSoup(html_crong, 'html.parser')
    crong_line = soup_crong.findAll('a')


    crong_item = []



    for line in crong_line:
        crong_item.append(line.text)

    elec_first_link = 'http://e3home.cau.ac.kr/20141201/sub08/sub01_view.php?cpage=1&idx='
    elec_last_link = '&search_gbn=3&search_keyword='
    
    elec_item_dict = {}

    elec_row = soup.findAll('td', {"width": "455", "class": "nbold"})

    for items in elec_row:
        elec_line = items.select('a')
        elec_item = elec_line[0].text
        # print(elec_item)
        if elec_item not in crong_item:
            elec_link_str = str(elec_line)
            elec_num_link = elec_link_str[30:33]
            elec_item_link = elec_first_link + elec_num_link + elec_last_link
            # print(elec_item_link)
            elec_item_dict[elec_item] = elec_item_link


    return elec_item_dict


def parse_social():
    ## setup Driver|Chrome : 크롬드라이버를 사용하는 driver 생성
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")


    driver = webdriver.Chrome(r'C:\Users\Dabui\Desktop\practice\chromedriver_win32\chromedriver.exe', chrome_options=options)
    driver.implicitly_wait(3)  ## 암묵적으로 웹 자원을 (최대) 3초 기다리기
    ## Login
    driver.get('http://society.cau.ac.kr/community/notice/List.asp')  # 중앙대학교 메인 홈페이지 공지사항 페이지 불러오기

    time.sleep(3)  # html 전체를 제대로 불러오기 위해 3초간 기다립니다

    html = driver.page_source  # 불러온 페이지의 html 소스들을 html이라는 변수에 할당

    soup = BeautifulSoup(html, 'html.parser')
    
    driver.get('http://localhost:8000/')
    time.sleep(1)
    html_crong = driver.page_source
    soup_crong = BeautifulSoup(html_crong, 'html.parser')
    crong_line = soup_crong.findAll('a')


    crong_item = []



    for line in crong_line:
        crong_item.append(line.text)
    
    social_first_link = 'http://society.cau.ac.kr/community/notice/'
    social_item_dict = {}

    social_row = soup.findAll('td', {"align": "left", "class": "bottom", "style": "padding-left:10px"})
    for items in social_row:
        social_line = items.select('a')
        social_item = social_line[0].text
        if social_item not in crong_item:
            social_url = items.find('a')
            social_url_link = str(social_url.attrs['href'])
            social_item_link = social_first_link + social_url_link
            social_item_dict[social_item] = social_item_link

    return social_item_dict


def parse_bis():


    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")


    driver = webdriver.Chrome(r'C:\Users\Dabui\Desktop\practice\chromedriver_win32\chromedriver.exe', chrome_options=options)
    driver.implicitly_wait(3)  ## 암묵적으로 웹 자원을 (최대) 3초 기다리기
    ## Login
    driver.get('http://bne.cau.ac.kr/bneNews/notice/list.php')  # 중앙대학교 메인 홈페이지 공지사항 페이지 불러오기

    time.sleep(3)  # html 전체를 제대로 불러오기 위해 3초간 기다립니다

    html = driver.page_source  # 불러온 페이지의 html 소스들을 html이라는 변수에 할당

    soup = BeautifulSoup(html, 'html.parser')

    driver.get('http://localhost:8000/')
    time.sleep(1)
    html_crong = driver.page_source
    soup_crong = BeautifulSoup(html_crong, 'html.parser')
    crong_line = soup_crong.findAll('a')


    crong_item = []



    for line in crong_line:
        crong_item.append(line.text)
    
    bis_first_link = 'http://bne.cau.ac.kr/bneNews/notice/view.php?page=1&s_key=&s_word=&idx='
    bis_item_dict = {}

    bis_row = soup.findAll('td', {"class": "subject"})
    for items in bis_row:
        bis_line = items.select('a')
        bis_item = bis_line[0].text
        if bis_item not in crong_item:
            bis_link_str = str(bis_line)
            bis_num_link = bis_link_str[73:76]
            bis_item_link = bis_first_link + bis_num_link
            # print(bis_item_link)
            bis_item_dict[bis_item] = bis_item_link

    return bis_item_dict

def parse_cmpeng():



    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")


    driver = webdriver.Chrome(r'C:\Users\Dabui\Desktop\practice\chromedriver_win32\chromedriver.exe', chrome_options=options)
    driver.implicitly_wait(3)  ## 암묵적으로 웹 자원을 (최대) 3초 기다리기
    ## Login
    ## setup Driver|Chrome : 크롬드라이버를 사용하는 driver 생성
    driver.get('http://localhost:8000/')  # 중앙대학교 메인 홈페이지 공지사항 페이지 불러오기

    time.sleep(3)  # html 전체를 제대로 불러오기 위해 3초간 기다립니다

    html = driver.page_source  # 불러온 페이지의 html 소스들을 html이라는 변수에 할당

    soup = BeautifulSoup(html, 'html.parser')

    driver.get('http://caucrongcrong.pythonanywhere.com/')
    time.sleep(1)
    html_crong = driver.page_source
    soup_crong = BeautifulSoup(html_crong, 'html.parser')
    crong_line = soup_crong.findAll('a')


    crong_item = []



    for line in crong_line:
        crong_item.append(line.text)
        
    cmpeng_first_link = 'http://cse.cau.ac.kr/20141201/sub05/sub0501.php?dir=bbs&nmode=view&code=oktomato_bbs05&uid='
    cmpeng_last_link = '&search=&keyword=&temp1=&offset=1'
    cmpeng_item_dict = {}

    cmpeng_row = soup.findAll('td', {"width": "48%"})
    for items in cmpeng_row:
        cmpeng_line = items.select('a')
        compeng_li = items.select('align')
        if cmpeng_line != compeng_li:
            old1_cmpeng_item = cmpeng_line[0].text
            if old1_cmpeng_item not in crong_item:
                old2_cmpeng_item = old1_cmpeng_item.replace('\n\t\t\t', '')
                cmpeng_item = old2_cmpeng_item.replace('\t\t\t\t\t\t\t\t', '')
                cmpeng_link_str = str(cmpeng_line)
                cmpeng_num_link = cmpeng_link_str[66:69]
                cmpeng_item_link = cmpeng_first_link + cmpeng_num_link + cmpeng_last_link
                # print(cmpeng_item_link)
                cmpeng_item_dict[cmpeng_item] = cmpeng_item_link

    return cmpeng_item_dict

if __name__=='__main__':
    cau_data_dict = parse_cau()
    for t, l in cau_data_dict.items():
        CauData(title=t, link=l).save()


    electric_data_dict = parse_electric()
    for t, l in electric_data_dict.items():
        ElectricData(title=t, link=l).save()



    social_data_dict = parse_social()
    for t, l in social_data_dict.items():
        SocialData(title=t, link=l).save()


    bis_data_dict = parse_bis()
    for t, l in bis_data_dict.items():
        BisData(title=t, link=l).save()

    cmpeng_data_dict = parse_cmpeng()
    for t, l in cmpeng_data_dict.items():
        CmpengData(title=t, link=l).save()