# import requests
# r = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(r.text, 'html.parser')
# # Everything Above is standard procedure into doing web scraping

# # Project specific code
# results = soup.find_all('span', attrs={'class':'short-desc'})

# first_result = results[0]
# print (first_result)

# first_result.find('strong')
# print ()
# print (first_result.find('strong'))
# print ()
# first_result.find('strong').text
# print (first_result.find('strong').text)
# print ()
# # might remove the line below due to how vs code reads the file that doesnt have NBSP
# first_result.find('strong').text[0:-1]
# print (first_result.find('strong').text[0:-1]) 
# print ()
# first_result.find('strong').text[0:-1]+', 2017'
# print (first_result.find('strong').text[0:-1]+', 2017')
# print ()
# first_result
# print (first_result)
# print ()
# first_result.contents
# print (first_result.contents)
# print ()
# first_result.contents[1]
# print (first_result.contents[1])
# print ()
# first_result.contents[1][1:-2]
# print (first_result.contents[1][1:-2])
# print ()
# first_result.contents[2]
# print (first_result.contents[2])
# print ()
# first_result.contents[2].text[1:-1]
# print (first_result.contents[2].text[1:-1])
# print ()
# first_result.find('a')
# print (first_result.find('a'))
# print ()
# first_result.find('a').text[1:-1]
# print (first_result.find('a').text[1:-1])
# print ()
# first_result.find('a')
# print (first_result.find('a'))
# print ()
# first_result.find('a')['href']
# print (first_result.find('a')['href'])
# print ()
# first_result.find('a')['target']
# print (first_result.find('a')['target'])
# print ()

# records = []
# for result in results:
#     date = result.find('strong').text[0:-1] + ', 2017'
#     lie = result.contents[1][1:-2]
#     explanation = result.find('a').text[1:-1]
#     url = result.find('a')['href']
#     records.append((date, lie, explanation, url))

# len(records)
# print (len(records))

# records[0:3]
# print (records[0:3])

# import pandas as pd
# df = pd.DataFrame(records, columns=['date', 'lie', 'explanation', 'url'])

# df.head()
# print(df.head())

# df.tail()
# print(df.tail())

# df['date'] = pd.to_datetime(df['date'])

# df.head()
# print(df.head())

# df.tail()
# print(df.tail())

# df.to_csv('trump_lies.csv', index=False, encoding='utf-8')
# df = pd.read_csv('trump_lies.csv', parse_dates=['date'], encoding='utf-8')

# summary of complete code 
import requests
r = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html') #read the website

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser') #convert website to HTML
results = soup.find_all('span', attrs={'class':'short-desc'}) #search all result in span with 'short-desc' tag

records = [] #open an empty tuple
for result in results:
    date = result.find('strong').text[0:-1] + ', 2017' #use strong tag to find date
    lie = result.contents[1][1:-2] #search 2nd content in a list to get lie
    explanation = result.find('a').text[1:-1] #alternatively can go: explanation = result.contents[2].text[1:-1] #use 'a' tag and .text to get explanation.
    url = result.find('a')['href'] #use a tag and under a tag sub element of href to find url
    records.append((date, lie, explanation, url)) #combine all result into a tuple

import pandas as pd
df = pd.DataFrame(records, columns=['date', ' lie', 'explanation', 'url']) #build a table with the column stated
df['date'] = pd.to_datetime(df['date']) #to standardize all date time format
df.to_csv('trump_lies.csv', index=False, encoding='utf-8') #to export data to CSV file

