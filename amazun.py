from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

browser = webdriver.Chrome()
browser.get("https://www.amazon.ae/s?k=tablet+samsung&sprefix=tablet+sa%2Caps%2C347&ref=nb_sb_ss_ts-doa-p_1_9")

price = browser.find_elements(By.CLASS_NAME, "a-price-whole")
names = browser.find_elements_by_css_selector("h2.s-line-clamp-4>a>span")
result=[["id","name","price"]]

for i in range(40):
    result.append([str(i),names[i].text,price[i].text])

with open("new_file.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(result)
browser.quit()
