from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os
import requests

# testing for page number
# r = requests.get('http://www.asiabuilders.com.my/company/list/all')
# soup = BeautifulSoup(r.text, 'html.parser') #can read html doc, but cannot get company list
# # company_lists = soup.find_all('article', attrs={'class':'comp-list'}) 
# # company_links = soup.find_all('a', attrs={'class':'d-block text-decoration-none p-2 mb-2 rounded'})
# # first_list = company_lists[0]
# print (company_links)
# closing of test page number



#launch url
url = "http://mpmadirectory.org.my/members_in_alphabetical_order"

#create a new Chrome session
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)
driver.get(url)

soup_level0 = BeautifulSoup(driver.page_source, 'lxml')

companylist = [] #empty list
a = 1 #counter

while a < 730:

    try:
        # Selenium visit each company page
        python_button = driver.find_element_by_xpath("//a[@href='http://mpmadirectory.org.my/member/"+str(a)+"']") # can visit each page and go back (cont)
        # but will stuck when a company page is empty and cannot go beyond the first alphabet
        python_button.click() #click link

        # For loop for each company goes here

        # Ask Selenium to click the back button
        driver.execute_script("window.history.go(-1)")

        #increment counter so it will keep going next page
        a += 1

    except ValueError:
        print("Company does not exists")
        

    #end of main loop

# driver.quit()









