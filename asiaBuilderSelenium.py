from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os
import requests

# testing for page number
# r = requests.get('http://www.asiabuilders.com.my/company/list/all')
# soup = BeautifulSoup(r.text, 'html.parser')
# pages = soup.find_all('tr', attrs={'class':'GridPager'})
# first_page = pages[0]
# print(first_page)
# closing of test page number

#testing for each company link
# r = requests.get('http://www.asiabuilders.com.my/company/list/all')
# soup = BeautifulSoup(r.text, 'html.parser')
# pages = soup.find_all('div', attrs={'class':'contenth3'})
# first_page = pages
# print(first_page)


#launch url
url = "http://www.asiabuilders.com.my/company/list/all"

#create a new Chrome session
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)
driver.get(url)

soup_level0 = BeautifulSoup(driver.page_source, 'lxml')


companylist = [] #empty list
a = 2 #counter

while a < 2108: #loop will go up until 2107 pages and stop

    # Selenium visit each page listing
    page_button = driver.find_element_by_xpath("//a[@href='/company/list/all/"+str(a)+"']") #xpath link for all pages
    page_button.click() #click link

    # Selenium hands the page source to Beautiful Soup
    soup_level1 = BeautifulSoup(driver.page_source, 'lxml')

    companylist.append([]) # an empty list in a bigger list
    x = 0 # counter

    r = requests.get('http://www.asiabuilders.com.my/company/list/all/2')
    soup = BeautifulSoup(r.text, 'html.parser')
    companies = soup.find_all('div', attrs={'class':'contenth3'})
    # print(companies)

    # Beautiful soup finds all the Company links on each page and the loop begins
    for company in companies: 

        # Selenium visits each Company Detail page
        company_button = driver.find_elements_by_xpath("//div[@class='contenth3']")[x] # for loop only going to 1st & 2nd item in list
        company_button.click() #click link

        # Loop for each company goes here

        
        # Ask Selenium to click the back button
        driver.execute_script("window.history.go(-1)") 

        # increment the counter variable before starting the loop over
        x += 1

        # end loop block


    #increment counter so it will keep going next page
    a += 1

    #end of main loop


driver.quit()









