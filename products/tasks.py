import logging
from celery import shared_task
from products.models import Product
from products.crawlers.products import WebProductScraper


@shared_task
def build_creat_and_update_products():
    logger = logging.getLogger(__name__)

    scraper = WebProductScraper()
    result = scraper.run()

    product_list = []
    product_codes = []

    for data in result:
        code = str(data["code"])
        product = Product(
            code=code,
            barcode=data["barcode"],
            status=data["status"],
            imported_t=data["imported_t"],
            url=data["url"],
            product_name=data["product_name"],
            quantity=data["quantity"],
            categories=data["categories"],
            packaging=data["packaging"],
            brands=data["brands"],
            image_url=data["image_url"]
        )
        product_list.append(product)
        product_codes.append(code)

    existing_products = Product.objects.filter(code__in=product_codes)
    existing_products_dict = {str(p.code): p for p in existing_products}

    updated_products = []
    created_products = []

    for product in product_list:
        code = str(product.code)
        if code in existing_products_dict:
            existing_product = existing_products_dict[code]
            existing_product.barcode = product.barcode
            existing_product.status = product.status
            existing_product.imported_t = product.imported_t
            existing_product.url = product.url
            existing_product.product_name = product.product_name
            existing_product.quantity = product.quantity
            existing_product.categories = product.categories
            existing_product.packaging = product.packaging
            existing_product.brands = product.brands
            existing_product.image_url = product.image_url
            existing_product.save()  # Atualizar o produto individualmente
            updated_products.append(existing_product)
        else:
            created_products.append(product)

    # Criar os produtos novos
    if created_products:
        try:
            Product.objects.bulk_create(created_products)
        except Exception as e:
            logger.error("Erro ao criar produtos novos: %s", str(e))

    logger.info("Execução da função build_and_update_products() concluída com sucesso.")
    return result
