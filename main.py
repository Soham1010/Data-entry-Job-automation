import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Google Sheets Link
# https://docs.google.com/spreadsheets/d/1VceLBDUJcvVO6yXhIDsUPE8qQ3AZIx6JKCYWakdB95g/edit?resourcekey=#gid=832871903


def fill_forms():

    for i in range(len(address_list)):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)

        driver = webdriver.Chrome(options=chrome_options)
        # driver.get('https://forms.gle/xxweASYuTFJ5G9bZ7')
        driver.get('https://forms.gle/JGmAu35JDkHjWC1aA')

        time.sleep(2)

        address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address.send_keys(address_list[i])

        price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price.send_keys(listing_price[i])

        list_link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        list_link.send_keys(listing_link[i])

        bttn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        bttn.click()
        time.sleep(1)

        driver.quit()


# -------------------------------------------------
# Fetch data from websites

response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
print(response.status_code)
website = response.text

soup = BeautifulSoup(website, 'html.parser')

anchor_links = soup.find_all('a', {'data-test':"property-card-link"})
listing_link = list(set([item.get('href') for item in anchor_links]))

ppty_price = soup.find_all('span', {'data-test':"property-card-price"})
listing_price = [item.text.strip() for item in ppty_price]

for item in range(len(listing_price)):
    listing_price[item] = listing_price[item].replace('1 bd', '')
    listing_price[item] = listing_price[item].replace('1bd', '')
    listing_price[item] = listing_price[item].replace('/mo', '')
    listing_price[item] = listing_price[item].replace('+', '')
    

address_soup = soup.find_all('address', {'data-test':"property-card-addr"})
address_list = [item.text.strip().replace('|', '') for item in address_soup]

# --------------------------------------------------
# Fill Forms

fill_forms()