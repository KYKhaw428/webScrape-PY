############################ IMPORTANT NOTICE ######################################
#### 1) This code can only be used for paid listing data scraped from asiabuilder website, \n
####    please seperate out between the paid and free listing data before running this code.
#### 2) Save asia builder file as xlsx format first before running this code.
#### 3) The need for this code to run is because the format of data being stored for paid listing are clumped into 1 column. \n
####    for example, the phone number, email, and adress are clumped in the 'Address' column when the data were scraped.


import pandas as pd
# tells panda to read the raw file
df = pd.read_excel('ABSeleniumRaw.xlsx') #change the name here according to the file name, or change the file name to match this one

# Building a new data frame by creating new columns, the data that existed from the 'Address' column will be split using line break method and stored into their respective new columns.
df[''], df[''], df[''], df['Reg No'], df['Address_new'], df['Phone Num'], df['Fax'], df['Email'] = df['Address'].str.split('\n', 7).str
# Delete the old 'Address' column after the data is being seperated.
del df['Address']

# Building a new data frame by creating new columns, the data that existed from the 'Contact' column will be split using line break method and stored into their respective new columns.
df[''], df[''], df['Misc_contact_1'], df['Misc_contact_2'],= df['Contact'].str.split('\n',3).str
# Delete the old 'Contact' column after the data is being seperated.
del df['Contact']

# Write the new dataframe into a new excel file in excel format
df.to_excel('ABSeleniumNewFormat.xlsx', index=False, encoding='utf-8') # New file name will follow anything that has been written here.

