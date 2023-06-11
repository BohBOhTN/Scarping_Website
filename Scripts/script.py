from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()


images_links = []
product_name = []
product_price = []
product_label = []
product_description = []
pages_links = ['https://www.carrefour.tn/default/mes-courses-alimentaires/boissons/jus.html?p=1','https://www.carrefour.tn/default/mes-courses-alimentaires/boissons/jus.html?p=2','https://www.carrefour.tn/default/mes-courses-alimentaires/boissons/jus.html?p=3']
def scrape_page(pages_links:list):

    driver.get(pages_links)

    list_products = driver.find_elements(By.XPATH,"//li[@class='item product product-item']")
    i=0
    for product in list_products:
        images_links.append(product.find_element(By.XPATH, ".//img").get_attribute("src"))
        product_name.append(product.find_element(By.XPATH,".//a[@class='product-item-link']").text)
        try:
            product_label.append(product.find_element(By.XPATH,".//a[@class='cr-brand-name']").text)
        except Exception as e:
            print(f"Couldn't find label for product {product_name[i]} error code")
            product_label.append('')
        product_description.append(product.find_element(By.XPATH,".//p[@class='cr-product-list-short-description-grid']").text)
        prix_dinar = product.find_element(By.XPATH,".//span[@class='cr-products-price-floor max-font-floor']").text
        prix_millime = product.find_element(By.XPATH,".//span[@class='cr-products-price-decimal-point max-font-decimal']").text
        prix_final = prix_dinar + "," + prix_millime
        product_price.append(prix_final)
        print(f"Just scraped the product {product_name[i]} Manifactured by {product_label[i]} And it costs {product_price[i]}")
        time.sleep(0.5)
        i += 1

for page in pages_links:
    scrape_page(page)


all_data_scraped = {
    'Product Name' : product_name,
    'Product Lable' : product_label,
    'Product Discription' : product_description,
    'Product Price' : product_price,
    'Product Image Link' : images_links
}

dataframe = pd.DataFrame(all_data_scraped)
dataframe.to_csv('Jus',index=False)



