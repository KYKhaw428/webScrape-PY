import requests
from bs4 import BeautifulSoup
import pandas as pd

companylist = ([])
n = 1

while n < 739:
    r = requests.get(f'http://mpmadirectory.org.my/member/{n}')

    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('li', attrs={'class':'col-lg-9 col-md-9 col-12 py-2'})

    try:
        name = results[0].text
    except IndexError:
        name = 'None'
    try:
        chief_exec = results[1].text
    except IndexError:
        chief_exec = 'None'
    try:
        ceo = results[2].text
    except IndexError:
        ceo = 'None'
    try:
        biz_enquiry = results[3].text
    except IndexError:
        biz_enquiry = 'None'
    try:
        biz_contact_person = results[4].text
    except IndexError:
        biz_contact_person = 'None'
    try:
        year_of_corp = results[5].text
    except IndexError:
        year_of_corp = 'None'
    try:
        address = results[6].text
    except IndexError:
        address = 'None'
    try:
        post_code = results[7].text
    except IndexError:
        post_code = 'None'
    try:
        city = results[8].text
    except IndexError:
        city = 'None'
    try:
        state = results[9].text
    except IndexError:
        state = 'None'
    try:
        country = results[10].text
    except IndexError:
        country = 'None'
    try:
        telephone = results[11].text
    except IndexError:
        telephone = 'None'
    try:
        fax = results[12].text
    except IndexError:
        fax = 'None'
    try:
        email = results[13].text
    except IndexError:
        email = 'None'
    try:
        website = results[14].text
    except IndexError:
        website = 'None'
    try:
        rawMat = results[15].text
    except IndexError:
        rawMat = 'None'
    try:
        prodProcess = results[16].text
    except IndexError:
        prodProcess = 'None'
    try:
        prodManufactured = results[17].text
    except IndexError:
        prodManufactured = 'None'
    try:
        miscData1 = results[18].text
    except IndexError:
        miscData1 = 'None'
    try:
        miscData2 = results[19].text
    except IndexError:
        miscData2 = 'None'
    try:
        miscData3 = results[20].text
    except IndexError:
        miscData3 = 'None'


    companylist.append((name, chief_exec, ceo, biz_enquiry, biz_contact_person, year_of_corp, address, post_code, city, state, country, telephone, fax, email, website, rawMat, prodProcess, prodManufactured, miscData1, miscData2, miscData3))
    
    n += 1


df = pd.DataFrame(companylist, columns=['Company', 'Chief Executive', 'CEO Position', 'Business Enquiry', 'Business Contact Person', 'Year of Incorporation', 'Office Address', 'PostCode', 'City/Town', 'State', 'Country', 'Telephone', 'Fax', 'Email', 'Website', 'Raw Materials Used', 'Production Process', 'Products Manufactured', 'Miscellaneous data 1', 'Miscellaneous data 2', 'Miscellaneous data 3'])
df.to_csv('MPMAdata.csv', index=False, encoding='utf-8')