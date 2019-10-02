from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os

# launch url
url = "http://kanview.ks.gov/PayRates/PayRates_Agency.aspx"

# create a new Chrome session
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)
driver.get(url)

soup_level0 = BeautifulSoup(driver.page_source, 'lxml')

agencylist = [] #empty list
a = 0 #counter

# After opening the url above, Selenium clicks the specific agency link
for agents in soup_level0.find_all('a', id=re.compile("^MainContent_uxLevel1_Agencies_uxAgencyBtn_")):

    # Selenium visits each Agency page
    python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_' + str(a))
    python_button.click() #click link

    # Selenium hands the page source to Beautiful Soup
    soup_level1 = BeautifulSoup(driver.page_source, 'lxml')

    agencylist.append([]) #an empty list in a bigger list
    x = 0 #counter

    # Beautiful Soup finds al the Job Title links on the agency page and the loop begins
    for link in soup_level1.find_all('a', id=re.compile("^MainContent_uxLevel2_JobTitles_uxJobTitleBtn_")):
        
        # Selenium visits each Job Title page
        python_button = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(x))
        python_button.click() #click link
        
        # Selenium hands of the source of the specific job page to Beautiful Soup
        soup_level2 = BeautifulSoup(driver.page_source, 'lxml')

        # Beautiful Soup grabs the HTML table on the page
        table = soup_level2.find_all('table')[0]

        # Giving the HTML table to pandas to put in a dataframe object
        df = pd.read_html(str(table), header=0)

        # Store the dataframe in a list
        agencylist.append(df[0])

        # Ask Selenium to click the back button
        driver.execute_script("window.history.go(-1)")

        # increment the counter variable before starting the loop over
        x += 1

        # end loop block

    # Store the each company's data frame in a bigger list
    # agencylist.append(datalist)
    
    # Ask Selenium to click the back button
    driver.execute_script("window.history.go(-1)")

    # increment the counter variable before starting the loop over
    a += 1

    # end of main loop

# loop has completed

# end the selenium browser session
driver.quit()

# combine all pandas dataframes in the list into one big dataframe
result = pd.concat([pd.DataFrame(agencylist[i]) for i in range(len(agencylist))],ignore_index=True)
result.to_csv('FSHUSelenium.csv', index=False, encoding='utf-8') #to export data to CSV file

# convert the pandas dataframe to JSON
# json_records = result.to_json(orient='records')

# pretty print to CLI with tabulate
# converts to an ascii table
# print(tabulate(result, headers=["Employee Name","Job Title","Overtime Pay","Total Gross Pay"],tablefmt='psql'))

# get current working directory
# path = os.getcwd()

# open, write, and close the file
# f = open(path + "\\fhsu_payroll_data.json", "w") #FHSU
# f.write(json_records)
# f.close

