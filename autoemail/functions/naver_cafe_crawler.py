import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re

__all__ = (
    'Naver_Cafe_Crawler',
)

class Naver_Cafe_Crawler():
    def scrape(self, url):
        url_text = requests.get(url)
        soup = BeautifulSoup(url_text.text, 'lxml')
        text = soup.find("a", {"id": "menuLink0"})
        PATTERN_URL = re.compile(r'href="(.*?)"')
        url_remainder = re.search(PATTERN_URL, str(text)).group(1)

        naver_id_list = []
        driver = webdriver.Chrome()
        for page_number in range(2)[1:2]:
            url_real = url + url_remainder + '&search.questionTab=A&search.totalCount=151&search.page=' + str(
                page_number)
            driver.get(url_real)
            time.sleep(3)
            driver.switch_to.frame('cafe_main')
            time.sleep(4)
            a = driver.find_element_by_tag_name('html')
            b = a.get_attribute('innerHTML')

            soup = BeautifulSoup(b, 'lxml')
            nick_tr_list = soup.find('form', {'name': 'ArticleList'}).find_all('td', class_='p-nick')

            PATTERN_NAVER_ID = re.compile(r'id="article_(.*?)_')
            for tr in nick_tr_list:
                naver_id = re.search(PATTERN_NAVER_ID, str(tr)).group(1)
                if naver_id not in naver_id_list:
                    naver_id_list.append(naver_id)

        return naver_id_list
