from selenium import webdriver
import csv

driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")

driver.get('https://www.flipkart.com/search?q=mouse&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')

mouses = driver.find_elements_by_class_name("s1Q9rs")
prices = driver.find_elements_by_class_name("_30jeq3")
colors = driver.find_elements_by_class_name("_3Djpdu")
discounts = driver.find_elements_by_class_name("_3Ay6Sb")
ratings = driver.find_elements_by_class_name("_3LWZlK")

mouse_list = [mouse.text for mouse in mouses]
 
price_list = [int(price.text.replace(',','')[1:]) for price in prices]
 
color_list = [color.text.split(',')[-1] for color in colors] 
 
discount_list = [discount.text[:-5] for discount in discounts]
 
rating_list = [rating.text for rating in ratings]
 

final_list=[]

for index in range(0,len(mouse_list)-1):
     list = [mouse_list[index],int(price_list[index]),color_list[index],discount_list[index],rating_list[index]]
     final_list.append(list)

 
print(final_list)

with open('Flipkart_prod_details_selenium.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Product','Price','color','discount','rating'])
    writer.writerows(final_list)