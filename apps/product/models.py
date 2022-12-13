from django.db import models

from core.models import BaseModel, BaseImage


class Product(BaseModel):

    STATUS_SET = (
        ('1', 'В наличии'),
        ('2', 'Под заказ'),
        ('3', 'Ожидает поступления'),
        ('4', 'Нет в наличии'),
        ('5', 'Не производится')
    )

    name = models.CharField('Название продукта', max_length=256, blank=True, null=True)
    part_number = models.CharField('Артикуль товара', max_length=256, blank=True, null=True)
    price = models.DecimalField('Цена товара', max_digits=7, decimal_places=2, blank=True, null=True)
    status = models.CharField('Статус товара', choices=STATUS_SET, max_length=1, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class ProductImage(BaseImage):
    product = models.ForeignKey(
        Product,
        verbose_name='Изображение продукта', related_name='image',
        on_delete=models.SET_NULL, blank=True, null=True
    )
