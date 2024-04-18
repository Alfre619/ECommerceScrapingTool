import os  # Importa el módulo os
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dataclasses import dataclass

@dataclass
class Product:
    manufacturer: str
    title: str
    price: str

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def scrape_page(driver, page):
    url = f"https://www.thomann.de/gb/search_GF_electric_guitars.html?ls=100&pg={page}&hl=BLOWOUT"
    driver.get(url)
    products = driver.find_elements(By.CSS_SELECTOR, "div.product")

    results = []
    for item in products:
        manufacturer = item.find_element(By.CSS_SELECTOR, "span.title__manufacturer").text
        title = item.find_element(By.CSS_SELECTOR, "span.title__name").text
        price = item.find_element(By.CSS_SELECTOR, "div.product__price").text.strip()
        results.append(Product(manufacturer, title, price))
    return results


def save_to_csv(products):
    # Usa una ruta absoluta para el archivo CSV
    file_path = "/home/brandon/PycharmProjects/ECommerceScrapingTool/data/products.csv"
    with open(file_path, mode="a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for product in products:
            writer.writerow([product.manufacturer, product.title, product.price])

def main():
    driver = get_driver()
    try:
        all_products = []
        for x in range(1, 4):  # adjust the range as needed
            products = scrape_page(driver, x)
            all_products.extend(products)
        save_to_csv(all_products)
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
