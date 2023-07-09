import logging
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime


class WebProductScraper:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def run(self):
        pag = 1
        url = f'https://world.openfoodfacts.org/{pag}'
        max_items = 100

        session = requests.Session()
        response = session.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        products = soup.find_all('a', href=lambda href: href and href.startswith("/product/"))

        data_products = []
        item_count = 0

        for product in products:
            if item_count >= max_items:
                pag += 1
                url = f'https://world.openfoodfacts.org/{pag}'
                response = session.get(url)
                soup = BeautifulSoup(response.content, "html.parser")
                products = soup.find_all('a', href=lambda href: href and href.startswith("/product/"))
                item_count = 0

            url_product_detail = f'https://world.openfoodfacts.org{product.get("href")}'

            response = session.get(url_product_detail)
            soup = BeautifulSoup(response.content, "html.parser")

            quantity = soup.find('span', class_='field_value', id='field_quantity_value').contents[0]
            barcode_paragraph = soup.find('p', id='barcode_paragraph')
            barcode_paragraph_text = barcode_paragraph.text if barcode_paragraph else ""
            barcode_match = re.search(r'Barcode:\s+(\d+)', str(barcode_paragraph_text))

            code = barcode_match.group(1) if barcode_match else None
            barcode = barcode_match.string.strip().split(':')[-1] if barcode_match else None

            product_name = soup.find('h1', class_='title-3', itemprop='name', property='food:name').text
            categories = soup.find(id='field_categories_value').text
            packaging_element = soup.find(id='field_packaging_value')
            packaging = packaging_element.text if packaging_element else None

            brands = soup.find(id='field_brands_value').text
            regex_pattern = r"^(...)(...)(...)(.*)$"

            match = re.match(regex_pattern, str(code))

            formatted_code_url_img = "/".join(match.groups()) if match else None if code else None
            try:
                image_url = soup.find(id='og_image').get('src')
            except:
                image_url = f"https://images.openfoodfacts.org/images/products/{formatted_code_url_img}/front_en.797.400.jpg" if formatted_code_url_img else None

            now = datetime.now()
            imported_t = now.strftime("%Y-%m-%dT%H:%M:%SZ")

            if all([quantity, code, barcode, product_name, categories, packaging, brands, formatted_code_url_img,
                    image_url]):

                data_products.append({
                    "code": code,
                    "barcode": barcode,
                    "status": "imported",
                    "imported_t": imported_t,
                    "url": url_product_detail,
                    "product_name": product_name,
                    "quantity": quantity,
                    "categories": categories,
                    "packaging": packaging,
                    "brands": brands,
                    "image_url": image_url
                })

                item_count += 1
                self.logger.info(f"Produto {item_count}: {product_name} -- {url_product_detail}")

            if item_count >= max_items:
                break

        return data_products


# Configurando o logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

