import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

companylist = ([])
n = 735

while n < 739:
    r = requests.get(f'http://mpmadirectory.org.my/member/{n}')

    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('li', attrs={'class':'col-lg-9 col-md-9 col-12 py-2'})

    name = results[0].text
    chief_exec = results[1].text
    ceo = results[2].text
    biz_enquiry = results[3].text
    biz_contact_person = results[4].text
    year_of_corp = results[5].text
    address = results[6].text
    post_code = results[7].text
    city = results[8].text
    state = results[9].text
    country = results[10].text
    telephone = results[11].text
    fax = results[12].text
    email = results[13].text
    companylist.append((name, chief_exec, ceo, biz_enquiry, biz_contact_person, year_of_corp, address, post_code, city, state, country, telephone, fax, email))
    
    n += 1



df = pd.DataFrame(companylist, columns=['Company', 'Chief Executive', 'CEO Position', 'Business Enquiry', 'Business Contact Person', 'Year of Incorporation', 'Office Address', 'PostCode', 'City/Town', 'State', 'Country', 'Telephone', 'Fax', 'Email'])
df.to_csv('MPMAdata.csv', index=False, encoding='utf-8')