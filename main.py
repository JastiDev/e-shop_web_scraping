from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("--window-size=1024,768")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service
                          (ChromeDriverManager().install()),
                          options=options)

base_url = "https://www.ebay.com/b/PC-Laptops-Netbooks/177/bn_317584?_pgn="

num_pages = 5

for page in range(1, num_pages + 1):
    url = f"{base_url}{page}"
    driver.get(url)
    time.sleep(10)

    product_list = []
    products = driver.find_elements(By.CLASS_NAME, "brwrvr__item-card")

    for product in products:
        try:
            title = product.find_element(By.CLASS_NAME, "bsig__title__text").text
        except:
            title = "Title not found"

        try: 
            price = product.find_element(By.CLASS_NAME, "bsig__price").text
        except:
            price = "Price not found"

        product_list.append([title, price])

driver.quit()

df = pd.DataFrame(product_list, columns=["Product Name", "Price"])

df.to_csv("ebay_products.csv", index=True, encoding="utf-8")

print("CSV file saved successfully.")