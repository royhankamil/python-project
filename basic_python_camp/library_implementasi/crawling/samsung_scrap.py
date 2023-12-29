import pandas as pd 
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

def search_elemet(item, tag, tClass):
    try:
        return item.find(tag, class_=tClass).text
    except:
        return ''
    
url = 'https://www.tokopedia.com/search?st=&q=samsung%20a8&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource='
driver = webdriver.Chrome()
driver.get()




