import requests
from bs4 import BeautifulSoup
import pandas as pd

co_details = ([])
# n = 1

# while n < 739:
r = requests.get('http://www.asiabuilders.com.my/company/details/50000657/tongue-groove-sdn-bhd')

soup = BeautifulSoup(r.text, 'html.parser')
# coName = soup.find_all('div', attrs={'class':'coprofileh3'}) #('table')[7].find_all('td') #attrs={'id':'content'}) #company Name found
# print(coName)
details = soup.find('table', attrs={'width':'660'}) #capture data from the table

name = details.contents[1].text
address = details.contents[3].text
contact = details.contents[5].text

co_details.append((name, address, contact))



df = pd.DataFrame(co_details, columns=['Name', 'Address', 'Contact'])
df.to_csv('AsiaBuildersdata.csv', index=False, encoding='utf-8')

######### To Do List ############
#1)able to retrieve data, got to  seperate data with excel.
#2)put data extracted into while loop
#3)collect data from other columns incase theres data available. (using try and accept)
#4)prepare another set of scrip for free listing companies


# print(details.contents[1].text) #managed to get company name
# print(details.contents[3].text) #managed to get company details from table
# print(details.contents[5].text) #managed to get contact from table


    # tag =  soup.find_all('li', attrs={'class':'col-lg-3 col-md-3 col-12 py-2 font-weight-bold'})

#     try:
#         colA1 = tag[0].text
#     except IndexError:
#         colA1 = 'None'
#     try:
#         name = results[0].text
#     except IndexError:
#         name = 'None'
#     try:
#         colA2 = tag[1].text
#     except IndexError:
#         colA2 = 'None'
#     try:
#         chief_exec = results[1].text
#     except IndexError:
#         chief_exec = 'None'
#     try:
#         colA3 = tag[2].text
#     except IndexError:
#         colA3 = 'None'
#     try:
#         ceo = results[2].text
#     except IndexError:
#         ceo = 'None'
#     try:
#         colA4 = tag[3].text
#     except IndexError:
#         colA4 = 'None'
#     try:
#         biz_enquiry = results[3].text
#     except IndexError:
#         biz_enquiry = 'None'
#     try:
#         colA5 = tag[4].text
#     except IndexError:
#         colA5 = 'None'
#     try:
#         biz_contact_person = results[4].text
#     except IndexError:
#         biz_contact_person = 'None'
#     try:
#         colA6 = tag[5].text
#     except IndexError:
#         colA6 = 'None'
#     try:
#         year_of_corp = results[5].text
#     except IndexError:
#         year_of_corp = 'None'
#     try:
#         colA7 = tag[6].text
#     except IndexError:
#         colA7 = 'None'
#     try:
#         address = results[6].text
#     except IndexError:
#         address = 'None'
#     try:
#         colA8 = tag[7].text
#     except IndexError:
#         colA8 = 'None'
#     try:
#         post_code = results[7].text
#     except IndexError:
#         post_code = 'None'
#     try:
#         colA9 = tag[8].text
#     except IndexError:
#         colA9 = 'None'
#     try:
#         city = results[8].text
#     except IndexError:
#         city = 'None'
#     try:
#         colA10 = tag[9].text
#     except IndexError:
#         colA10 = 'None'
#     try:
#         state = results[9].text
#     except IndexError:
#         state = 'None'
#     try:
#         colA11 = tag[10].text
#     except IndexError:
#         colA11 = 'None'
#     try:
#         country = results[10].text
#     except IndexError:
#         country = 'None'
#     try:
#         colA12 = tag[11].text
#     except IndexError:
#         colA12 = 'None'
#     try:
#         telephone = results[11].text
#     except IndexError:
#         telephone = 'None'
#     try:
#         colA13 = tag[12].text
#     except IndexError:
#         colA13 = 'None'
#     try:
#         fax = results[12].text
#     except IndexError:
#         fax = 'None'
#     try:
#         colA14 = tag[13].text
#     except IndexError:
#         colA14 = 'None'
#     try:
#         email = results[13].text
#     except IndexError:
#         email = 'None'
#     try:
#         colA15 = tag[14].text
#     except IndexError:
#         colA15 = 'None'
#     try:
#         website = results[14].text
#     except IndexError:
#         website = 'None'
#     try:
#         colA16 = tag[15].text
#     except IndexError:
#         colA16 = 'None'
#     try:
#         rawMat = results[15].text
#     except IndexError:
#         rawMat = 'None'
#     try:
#         colA17 = tag[16].text
#     except IndexError:
#         colA17 = 'None'
#     try:
#         prodProcess = results[16].text
#     except IndexError:
#         prodProcess = 'None'
#     try:
#         colA18 = tag[17].text
#     except IndexError:
#         colA18 = 'None'
#     try:
#         prodManufactured = results[17].text
#     except IndexError:
#         prodManufactured = 'None'
#     try:
#         colA19 = tag[18].text
#     except IndexError:
#         colA19 = 'None'
#     try:
#         miscData1 = results[18].text
#     except IndexError:
#         miscData1 = 'None'
#     try:
#         colA20 = tag[19].text
#     except IndexError:
#         colA20 = 'None'
#     try:
#         miscData2 = results[19].text
#     except IndexError:
#         miscData2 = 'None'
#     try:
#         colA21 = tag[20].text
#     except IndexError:
#         colA21 = 'None'
#     try:
#         miscData3 = results[20].text
#     except IndexError:
#         miscData3 = 'None'


#     companylist.append((colA1, name, colA2, chief_exec, colA3, ceo, colA4, biz_enquiry, colA5, biz_contact_person, colA6, year_of_corp, colA7, address, colA8, post_code, colA9, city, colA10, state, colA11, country, colA12, telephone, colA13, fax, colA14, email, colA15, website, colA16, rawMat, colA17, prodProcess, colA18, prodManufactured, colA19, miscData1, colA20, miscData2, colA21, miscData3))
    
#     n += 1


# df = pd.DataFrame(companylist, columns=['Description', 'Data', 'Description', 'Data', 'Description', 'Data', 'Description', 'Data', 'Description', 'Data', 'Description', 'Data', 'Description', 'Data', 'Description', 'Data', 'Description', 'Data', 'Description', 'Data', 'Description', 'Data', 'Description', 'Data', 'Description', 'Data', 'Description', 'Data', 'Description', 'Data', 'Description', 'Data', 'Description', 'Data', 'Description', 'Data', 'Description', 'Data', 'Description', 'Data', 'Description', 'Data'])
# df.to_csv('MPMAdata.csv', index=False, encoding='utf-8')