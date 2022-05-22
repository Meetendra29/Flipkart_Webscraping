import requests
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd

URL ="https://www.flipkart.com/search?q=mobiles+vivo+and+oppo&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_2_7_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_2_7_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobiles+vivo+and+oppo&requestId=3ca15874-e2ca-4dd5-87d8-9b45fde58dc9&as-searchtext=mobiles"
header= {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
"Accept-Language":"en-US,en;q=0.9,hi;q=0.8"

}
response = requests.get(URL, headers=header)

soup = bs(response.content,"html.parser")

#print(soup.prettify())

names = soup.find_all(name = "div", class_="_4rR01T")
prices = soup.find_all(name ="div", class_="_30jeq3 _1_WHN1")
#print(names)

names_list = [name.getText() for name in names]
price_list = [int(price.getText().strip()[1:].replace(',','')) for price in prices]
#for name in names:
#    text = name.getText()
#    names_list.append(text)

#print(names_list)
#print(price_list)

final_list=[]

for index in range(0,len(price_list)-1):
     list = [names_list[index],int(price_list[index])]
     final_list.append(list)

#print(final_list)

#method 1
with open('Product_price_list.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Product','Price'])
    writer.writerows(final_list)

# method 2
#df = pd.DataFrame(final_list)
#df.to_csv('file2.csv', index = False, header=['Product','Price'])

# method 3  PURE PYTHON

#with open('file3.csv','w') as f:
#    for row in final_list:
#        for x in row:
#            f.write(str(x)+',')
#        f.write('\n')