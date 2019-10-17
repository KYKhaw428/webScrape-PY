from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os
import requests


#launch url
url = "http://www.asiabuilders.com.my/company/list/all/" #change the page number for the url if the code breaks so it continues from where the code stops \n
# for example, if the code stops at page 101 change the entire url to "http://www.asiabuilders.com.my/company/list/all/100"

#create a new Chrome session
options = Options() 
options.headless = True #to make browser headless
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options) #Browser operating in headless aka no pop up and unable to see the navigation.
driver.implicitly_wait(30)
driver.get(url)

soup_level0 = BeautifulSoup(driver.page_source, 'lxml')


companylist = ([]) #empty list
pageNumber = 2 #counter #change the page counter for if the code breaks so u can continue from where it stops.\n
# for example, if breaks at page 101, u change the code to pageNumber = 101

while pageNumber < 2108: #loop will go up until 2107 pages and stop

    # Selenium visit each page listing
    page_button = driver.find_element_by_xpath("//a[@href='/company/list/all/"+str(pageNumber)+"']") #xpath link for all pages
    page_button.click() #click link

    # Selenium hands the page source to Beautiful Soup
    soup_level1 = BeautifulSoup(driver.page_source, 'lxml')

    listSelector = 0 # counter

    # Use requests to get each page on the website
    r = requests.get(f'http://www.asiabuilders.com.my/company/list/all/{pageNumber}')
    # Use beautifulsoup to parse the entire web page in text form
    soup = BeautifulSoup(r.text, 'html.parser')
    # Create a variable to store company of each page in a list under the div tag element of class: "contenth3"
    companies = soup.find_all('div', attrs={'class':'contenth3'})

    # Beautiful soup finds all the Company links on each page and the loop begins
    for company in companies: 

        # Selenium visits each Company Detail page
        parentElement = driver.find_elements_by_class_name("contenth3")[listSelector] #Tells driver to search for class with "contenth3" and iterate through listSelector counter variable
        link = parentElement.find_element_by_tag_name("a") #Finds all the link under the parent element
        link.click() #click link

        # Create a variable to store the current page url that the driver is currently navigating, which is each company detail page
        individual_url = driver.current_url
        # Use requests to get the URL so that so that beautifulsoup can convert it to text
        read = requests.get(individual_url)
        # BeautifulSoup parse the current driver URL into text
        soup_level2 = BeautifulSoup(read.text, 'html.parser')
        # A variable to store all company details which are paid listing and has the table tag element of width: "660"
        details1 = soup_level2.find('table', attrs={'width':'660'})
        # Another variable to store all company details which are free listing and has the table tag element of cellspacing: "5"
        details2 = soup_level2.find('table', attrs={'cellspacing':'5'})


        # Try and except is being used when scraping between paid listing and free listing
        # Python will first try to search for paid listing pages, if no details for paid listing companies are found, \n
        # the code will continue to run with the exception of AttributeError, \n
        # and the code will try to search for free listing company page details. \n
        # Lastly, if the individual page company does not consists of either paid or free listing details, it will be stored as an empty data.
        try:
            name = details1.contents[1].text # Storing paid company name in a variable that is index 1 in the list of table
        except AttributeError:
            try:
                name = details2.contents[1].text # Storing free company name in a variable that is index 1 in the list of table
            except AttributeError:
                name = '' # Storing data as blank if either paid of free listing does not exists in the page.
        try:
            address = details1.contents[3].text # Storing paid company address in a variable that is index 3 in the list of table
        except AttributeError:
            try:
                address = details2.contents[5].text # Storing free company address in a variable that is index 5 in the list of table
            except AttributeError:
                address = '' # Storing data as blank if either paid of free listing does not exists in the page.
        try:
            contact = details1.contents[5].text # Storing paid company contact in a variable that is index 5 in the list of table
        except AttributeError:
            try:
                contact = details2.contents[9].text # Storing free company contact in a variable that is index 9 in the list of table
            except AttributeError:
                contact = '' # Storing data as blank if either paid of free listing does not exists in the page.
        try:
            misc = details1.contents[7].text # Storing paid company miscellaneous data in a variable that is index 7 in the list of table
        except AttributeError:
            try:
                misc = details2.contents[17].text # Storing free company miscellaneous dat in a variable that is index 17 in the list of table
            except AttributeError:
                misc = '' # Storing data as blank if either paid of free listing does not exists in the page.

        # Putting all the individual variable in a list
        companylist.append((name, address, contact, misc))


        # Ask Selenium to click the back button
        driver.execute_script("window.history.go(-1)") 

        # increment the counter variable so it will keep going to the next individual company URL before starting the loop over
        listSelector += 1
        # Since headless browser is being used, this will be an indicator in the terminal of the web scraping process for each company that the browser went through.
        print(f'company{listSelector}')


        # Using pandas create a dataframe from the list we appended and specifying the columns
        # This part is included in the loop so the file will be constantly updated, even when the code breaks the file will have the most recent data. \n
        # Save the most recent file in a different name if the code breaks and re run the code by changing the counter variable 'pageNumber' from where it stops.
        df = pd.DataFrame(companylist, columns=['Name', 'Address', 'Contact', 'Misc'])
        # Writing the dataframe into a CSV file
        df.to_csv('ABSeleniumRaw.csv', index=False, encoding='utf-8')


        # end loop block


    #increment counter so it will keep going next page
    pageNumber += 1
    # Since headless browser is being used, this will be an indicator in the terminal of the web scraping process for each page that the browser went through.
    print(f'page{pageNumber}')


    #end of main loop


driver.quit()








