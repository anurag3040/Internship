#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import time


# In[ ]:


# first connect to the driver
driver=webdriver.Chrome(r"C:\Users\AnuragMishra\Downloads\chromedriver_win32.exe")


# # 1. Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.naukri.com/
# 2. Enter “Data Analyst” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.

# In[ ]:


# opening the naukari page on selenium automated chrome browser
driver.get("https://www.naukri.com/")


# In[ ]:


# entering the Job position & Location as required
designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Analyst')


# In[ ]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Bangalore')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[ ]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[ ]:


#scrapping job title from naukari page
title1 = driver.find_elements(By.XPATH, '//a[@class="title ellipsis"]')
for i in title1[0:10]:
    title=i.text
    job_title.append(title)

#scrapping job location from naukari page
location1 = driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft locWdth"]')
for i in location1[0:10]:
    location=i.text
    job_location.append(location)

#scrapping company name from naukari page
company1 = driver.find_elements(By.XPATH, '//a[@class="subTitle ellipsis fleft"]')
for i in company1[0:10]:
    company=i.text
    company_name.append(company)

#scrapping experience required from naukari page
experience1 = driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft expwdth"]')
for i in experience1[0:10]:
    exp=i.text
    experience_required.append(exp)


# In[ ]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[ ]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company_name,'Experience':experience_required})
df


# # 2. Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.naukri.com/
# 2. Enter “Data Scientist” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.

# In[ ]:


# first connect to the driver
driver=webdriver.Chrome(r"C:\Users\AnuragMishra\Downloads\chromedriver_win32.exe")
# opening the naukari page on selenium automated chrome browbScrapping\chromedriver.exe")


# In[ ]:


# opening the naukari page on selenium automated chrome browser
driver.get("https://www.naukri.com/")


# In[ ]:


# entering the Job position & Location as required
position=driver.find_element(By.CLASS_NAME,"suggestor-input")
position.send_keys('Data Scientist')


# In[ ]:


location2=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location2.send_keys('Bangalore')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[ ]:


job_title1=[]
job_location1=[]
company_name1=[]


# In[ ]:


#scrapping job title from naukari page
title2 = driver.find_elements(By.XPATH, '//a[@class="title ellipsis"]')
for i in title2[0:10]:
    title=i.text
    job_title1.append(title)

#scrapping job location from naukari page
location3 = driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft locWdth"]')
for i in location3[0:10]:
    location2=i.text
    job_location1.append(location2)

#scrapping company name from naukari page
company2 = driver.find_elements(By.XPATH, '//a[@class="subTitle ellipsis fleft"]')
for i in company2[0:10]:
    company=i.text
    company_name1.append(company)


# In[ ]:


print(len(job_title1),len(job_location1),len(company_name1))


# In[ ]:


import pandas as pd
df1=pd.DataFrame({'Title':job_title1,'Location':job_location1,'Company':company_name1})
df1


# # 3. In this question you have to scrape data using the filters available on the webpage as shown below:
# You have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results.
# You have to scrape the job-title, job-location, company name, experience required.
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
# The task will be done as shown in the below steps:
# 1. first get the webpage https://www.naukri.com/
# 2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
# 3. Then click the search button.
# 4. Then apply the location filter and salary filter by checking the respective boxes
# 5. Then scrape the data for the first 10 jobs results you get.
# 6. Finally create a dataframe of the scraped data.

# In[ ]:


# first connect to the driver
driver=webdriver.Chrome(r"C:\Users\AnuragMishra\Downloads\chromedriver_win32.exe")


# In[ ]:


# opening the naukari page on selenium automated chrome browser
driver.get("https://www.naukri.com/")


# In[ ]:


# entering the Job position & Location as required
position=driver.find_element(By.CLASS_NAME,"suggestor-input")
position.send_keys('Data Scientist')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[ ]:


location_delhi=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[5]/div[2]/div[2]/label/i")
location_delhi.click()
# filter1=driver.find_element(By.XPATH,'//i[@class="fleft naukicon naukicon-checkbox"]')
# filter1.click()
# location_search_box = driver.find_element(By.CLASS_NAME, 'filterOptns')
# location_search_box.clear()  # clear any existing text in the search box
# location_search_box.send_keys('Delhi/NCR')


# In[ ]:


salary=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[6]/div[2]/div[2]/label/i")
salary.click()


# In[ ]:


job_title1=[]
job_location1=[]
company_name1=[]
experience_required1=[]


# In[ ]:


#scrapping job title from naukari page
title2 = driver.find_elements(By.XPATH, '//a[@class="title ellipsis"]')
for i in title2[0:10]:
    titles=i.text
    job_title1.append(titles)

#scrapping job location from naukari page
location2 = driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft locWdth"]')
for i in location2[0:10]:
    locations=i.text
    job_location1.append(locations)

#scrapping company name from naukari page
company2 = driver.find_elements(By.XPATH, '//a[@class="subTitle ellipsis fleft"]')
for i in company2[0:10]:
    companys=i.text
    company_name1.append(companys)

#scrapping experience required from naukari page
experience2 = driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft expwdth"]')
for i in experience2[0:10]:
    exp1=i.text
    experience_required1.append(exp1)


# In[ ]:


df2=pd.DataFrame({'Title':job_title1,'Location':job_location1,'Company':company_name1,'Experience':experience_required1})
df2


# # 4. Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 1. Brand
# 2. Product Description
# 3. Price
# 
# To scrape the data you have to go through following steps:
# 1. Go to Flipkart webpage by url : https://www.flipkart.com/
# 2. Enter “sunglasses” in the search field where “search for products, brands and more” is written and
# click the search icon
# 3. After that you will reach to the page having a lot of sunglasses. From this page you can scrap the
# required data as usual.
# 4. After scraping data from the first page, go to the “Next” Button at the bottom other page , then
# click on it.
# 5. Now scrape data from this page as usual
# 6. Repeat this until you get data for 100 sunglasses.

# In[ ]:


# first connect to the driver
driver=webdriver.Chrome(r"C:\Users\AnuragMishra\Downloads\chromedriver_win32.exe")


# In[ ]:


# opening the flipkart page on selenium automated chrome browser
driver.get("https://www.flipkart.com/")


# In[ ]:


# entering the Job position & Location as required
products=driver.find_element(By.CLASS_NAME,"_3704LK")
products.send_keys('sunglasses')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,"_34RNph")
search.click()


# In[ ]:


brand = []
description = []
price = []


# In[ ]:


#scrapping brand from flipkart page
start = 0
end = 3
brand1 = driver.find_elements(By.CLASS_NAME, '_2WkVRV')
for i in brand1:
    brands=i.text
    brand.append(brands)
brand_name = brand[0:100]

#scrapping description from flipkart page
start = 0
end = 3
description1 = driver.find_elements(By.CLASS_NAME, 'IRpwTa')
for i in description1:
    descriptions=i.text
    description.append(descriptions)
description2 = description[0:100]

#scrapping price from flipkart page
start = 0
end = 3
price1 = driver.find_elements(By.CLASS_NAME, '_30jeq3')
for i in price1:
    prices=i.text
    price.append(prices)
price2 = price[0:100]


# In[ ]:


print(len(brand_name), len(description2), len(price2))


# In[ ]:


df3=pd.DataFrame({'Brand':brand_name,'Description':description2,'Price':price2})
df3


# # 5. Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link:
# https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART
# As shown in the above page you have to scrape the tick marked attributes. These are:
# 1. Rating
# 2. Review summary
# 3. Full review
# 4. You have to scrape this data for first 100 reviews.

# In[ ]:


# first connect to the driver
driver=webdriver.Chrome(r"C:\Users\AnuragMishra\Downloads\chromedriver_win32.exe")


# In[ ]:


# opening the flipkart given page on selenium automated chrome browser
# given link in the ques is not available or product removed from website
driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/p/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART&q=iphone+11&store=tyy%2F4io&srno=s_1_4&otracker=search&otracker1=search&fm=organic&iid=77b69675-8ec5-4d27-8a2b-0aca89ef221e.MOBFWQ6BXGJCEYNY.SEARCH&ppt=hp&ppn=homepage&ssid=ktv3hdy93k0000001683543269877&qH=f6cdfdaa9f3c23f3")


# In[ ]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[10]/div[7]/div/a/div/span")
search.click()


# In[ ]:


rating = []
summary = []
review = []


# In[ ]:


#scrapping brand from flipkart page
start = 0
end = 100
for page in range(start,end):
    rating1 = driver.find_elements(By.XPATH, '//div[@class="_3LWZlK _1BLPMq"]')
    for i in rating1:
        ratings=i.text
        rating.append(ratings)
    next_button = driver.find_element(By.XPATH, '//a[@class="_1LKTO3"]') #to scrap data from next pages
    next_button.click()
    time.sleep(5)


# In[ ]:


#scrapping brand from flipkart page
start = 0
end = 10
for page in range(start,end):
    summary1 = driver.find_elements(By.XPATH, '//p[@class="_2-N8zT"]')
    for i in summary1:
        summarys=i.text
        summary.append(summarys)
    next_button = driver.find_element(By.XPATH, '//span') #to scrap data from next pages
    next_button.click()
    time.sleep(10)


# In[ ]:


#scrapping brand from flipkart page
start = 0
end = 10
for page in range(start,end):
    review1 = driver.find_elements(By.XPATH, '//div[@class="t-ZTKy"]')
    for i in review1:
        reviews=i.text
        review.append(reviews)
    next_button = driver.find_element(By.XPATH, '//span') #to scrap data from next pages
    next_button.click()
    time.sleep(10)


# In[ ]:


print(len(review),len(summary),len(review))


# In[ ]:


df4=pd.DataFrame({'Rating':rating,'Summary':summary,'Full Review':review})
df4


# # 6. Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the search field. You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. Product Description
# 3. Price
# As shown in the below image, you have to scrape the above attributes.

# In[ ]:


# first connect to the driver
driver=webdriver.Chrome(r"C:\Users\AnuragMishra\Downloads\chromedriver_win32.exe")


# In[ ]:


# opening the flipkart given page on selenium automated chrome browser
driver.get("https://www.flipkart.com/")


# In[ ]:


product=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
product.send_keys('sneakers')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
search.click()


# In[ ]:


sneaker_brand = []
sneaker_description = []
brand11 = []
description11 = []


# In[ ]:


#scrapping brand from flipkart page
start = 0
end = 3
sbrand = driver.find_elements(By.CLASS_NAME, '_2WkVRV')
for i in sbrand:
    sbrand1=i.text
    sneaker_brand.append(sbrand1)
    
brand11 = sneaker_brand[0:100]

#scrapping description from flipkart page
start = 0
end = 3
sdescription = driver.find_elements(By.CLASS_NAME, 'IRpwTa')
for i in sdescription:
    sdescription1=i.text
    sneaker_description.append(sdescription1)
description11 = sneaker_description[0:100]


# In[ ]:


print(len(brand11), len(description11))


# In[ ]:


df5=pd.DataFrame({'Brand':brand11,'Description':description11})
df5


# # 9. Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead, Term of office, Remarks) from https://www.jagranjosh.com/.
# This task will be done in following steps:
# 1. First get the webpage https://www.jagranjosh.com/
# 2. Then You have to click on the GK option
# 3. Then click on the List of all Prime Ministers of India
# 4. Then scrap the mentioned data and make the DataFrame.

# In[473]:


# first connect to the driver
driver=webdriver.Chrome(r"C:\Users\AnuragMishra\Downloads\chromedriver_win32.exe")


# In[474]:


# opening the motor1 page on selenium automated chrome browser
driver.get("https://www.jagranjosh.com/")


# In[476]:


gk=driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[5]/div/div[1]/header/div[3]/ul/li[3]/a")
gk.click()


# In[478]:


pm=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[10]/div/div/ul/li[2]/a")
pm.click()


# In[482]:


# Find the table with the class 'table'
table = driver.find_elements(By.CLASS_NAME, 'table')
table


# In[503]:


pm_name = []
born_dead = []
term = []
remarks = []


# In[504]:


pm1 = driver.find_elements(By.TAG_NAME, "tr")
for i in pm1:
    pm2=i.text
    pm_name.append(pm2)
    
pm_name


# In[ ]:


# extract the four lists
names = []
born_dead = []
term_of_office = []
remarks = []

for item in pm_name[1:]:
    # split each line into a list of columns
    columns = item.split('\n')
    names.append(columns[1])
    born_dead.append(columns[2])
    term_of_office.append(columns[3])
    remarks.append(columns[4])

# print the four lists
print(names)
print(born_dead)
print(term_of_office)
print(remarks)


# In[472]:


pm_info_list = [pm.split('\n') for pm in pm_name[1:19]]

for pm_info in pm_info_list:
    name = pm_info[1]
    born_dead = pm_info[2]
    term = pm_info[3]
    remark = pm_info[4]
    print(f"{name}\n{born_dead}\n{term}\n{remark}\n")


# In[ ]:


df8 = pd.DataFrame(data)
df8


# # 10: Write a python program to display list of 50 Most expensive cars in the world (i.e. Car name and Price) from https://www.motor1.com/
# This task will be done in following steps:
# 1. First get the webpage https://www.motor1.com/
# 2. Then You have to click on the List option from Dropdown menu on left side.
# 3. Then click on 50 most expensive cars in the world..
# 4. Then scrap the mentioned data and make the dataframe.

# In[ ]:


# first connect to the driver
driver=webdriver.Chrome(r"C:\Users\AnuragMishra\Downloads\chromedriver_win32.exe")


# In[ ]:


# opening the motor1 page on selenium automated chrome browser
driver.get("https://www.motor1.com/")


# In[ ]:


search=driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div[3]/ul/li[6]/ul/li[1]/a")
search.click()


# In[ ]:


search1=driver.find_element(By.XPATH,"/html/body/div[3]/div[8]/div[1]/div[1]/div/div/div[7]/div/div[1]/h3/a")
search1.click()


# In[ ]:


name1 = []
price5 = []


# In[ ]:


car = driver.find_elements(By.XPATH, '//h3[@class="subheader"]')
for i in car:
    names=i.text
    name.append(names)
    
name1=name[51:101]
name1


# In[ ]:


price3 = driver.find_elements(By.XPATH, "//strong")
for i in price3:
    price4=i.text
    price5.append(price4)
    
price6 = price5[0:50]
price6


# In[ ]:


print(len(name1), len(price6))


# In[ ]:


df9=pd.DataFrame({'Car Name':name1,'Price':price6})
df9


# In[ ]:




