from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1024,768")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service
                          (ChromeDriverManager().install()),
                          options=options)

url = "https://www.ebay.com/b/Type-Chopper/6024/bn_57336502"
driver.get(url)

time.sleep(3)

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