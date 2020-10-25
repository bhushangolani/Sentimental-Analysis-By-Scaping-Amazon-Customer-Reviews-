import os
import csv
from bs4 import BeautifulSoup
import time
from selenium import webdriver
import math
import urllib
import timeit
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)


search_term = 'smartphone'
url= 'https://www.amazon.com/s?k=' + search_term + '&ref=nb_sb_noss_1'

time.sleep(15)

driver.get(url)
i=0
all_data=pd.DataFrame()
data=pd.DataFrame(columns=['Mobile'])
data1=pd.DataFrame(columns=['Mobile', 'Review'])

pgno=0


while i<100:
    pgno=pgno+1
    div_count = len(driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']"))
    mobile=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
    
    for z in range(0,len(mobile),1):
        data=data.append({'Mobile':[mobile[z].text.strip()]},ignore_index=True)
        

    for c in range (0,div_count,1):
       time.sleep(10)
       driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")[c].click()
       time.sleep(10)
     

       no_of_rev=len(driver.find_elements_by_xpath("//div[@class=\'a-expander-content reviewText review-text-content a-expander-partial-collapse-content\']/span"))
       time.sleep(5)
       name=driver.find_elements_by_xpath("//div[@class=\'a-expander-content reviewText review-text-content a-expander-partial-collapse-content\']/span")
       time.sleep(3)
       for rev in range(no_of_rev):
            data1=data1.append({'Mobile':data.iloc[c],'Review':[name[rev].text.strip()]},ignore_index=True)
       
       time.sleep(5)     
       all_data=all_data.append(data1)
       
       data2=pd.DataFrame(columns=['Mobile', 'Review'])
       data1=data2
       
       
       time.sleep(7)   
       if(len(driver.find_elements_by_xpath("//a[@id='breadcrumb-back-link']"))!=0):
           time.sleep(5)    
           driver.find_elements_by_xpath("//a[@id='breadcrumb-back-link']")[0].click()  
       else:
           search_term = 'smartphone'
           url= 'https://www.amazon.com/s?k=' + search_term + '&ref=nb_sb_noss_1'
           time.sleep(7)
           driver.get(url)
           for tt in range (0,pgno):
               time.sleep(5)
               driver.find_elements_by_xpath("//li[@class='a-last']")[0].click()
               time.sleep(3)
           
           
       time.sleep(7)
    
    
    data3=pd.DataFrame(columns=['Mobile'])
    data=data3
    time.sleep(7)
    driver.find_elements_by_xpath("//li[@class='a-last']")[0].click()   
    time.sleep(7)
    
    i=i+div_count     
    
all_data.to_csv('DATA.csv')    

