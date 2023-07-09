from django.db import models


class Product(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('imported', 'Imported'),
    ]

    code = models.BigIntegerField()  # Alteração para BigIntegerField
    barcode = models.CharField(max_length=550)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    imported_t = models.DateTimeField()
    url = models.URLField()
    product_name = models.CharField(max_length=550)
    quantity = models.CharField(max_length=550)
    categories = models.CharField(max_length=550)
    packaging = models.CharField(max_length=550)
    brands = models.CharField(max_length=550)
    image_url = models.URLField()

    def __str__(self):
        return self.code

    class Meta:
        ordering = ['-imported_t']
