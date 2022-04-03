import requests
from bs4 import BeautifulSoup
import lxml.html as lh
import pandas as pd

url = 'https://jadwalsholat.org/jadwal-sholat/monthly.php?id=168'
page = requests.get(url)

#Store the contents of the website under doc
doc = lh.fromstring(page.text)

#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')
print(len(tr_elements))
#Create empty list
col=[]
i=0

#For each row, store each first element (header) and an empty list
for t in tr_elements[3]:
    i+=1
    name=t.text_content()
    print('%d:"%s"'%(i,name))
    col.append((name,[]))
    
    
# #Check the length of the first 12 rows
[len(T) for T in tr_elements[3:20]]


#Create Pandas DataFrame
#Since out first row is the header, data is stored on the second row onwards
for j in range(4,len(tr_elements)):
    #T is our j'th row
    T=tr_elements[j]
    
    #If row is not of size 10, the //tr data is not from our table 
    if len(T)!=9:
        break
    
    #i is the index of our column
    i=0
    
    #Iterate through each element of the row
    for t in T.iterchildren():
        data=t.text_content() 
        #Check if row is empty
        if i>0:
        #Convert any numerical value to integers
            try:
                data=int(data)
            except:
                pass
        #Append the data to the empty list of the i'th column
        col[i][1].append(data)
        #Increment i for the next column
        i+=1
   
#check width column     
#[len(C) for (title,C) in col]

Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)
df[df['Tanggal']=='01']


