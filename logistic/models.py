from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=60, unique=True, verbose_name='наименование')
    description = models.TextField(null=True, blank=True, verbose_name='описание')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.title}'


class Stock(models.Model):
    address = models.CharField(max_length=200, unique=True, verbose_name='адрес')
    products = models.ManyToManyField(
        Product,
        through='StockProduct',
        related_name='stocks',
    )

    class Meta:
        verbose_name = 'склад'
        verbose_name_plural = 'склады'
        ordering = ['address']

    def __str__(self):
        return self.address


class StockProduct(models.Model):
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        related_name='positions',
        verbose_name='склад',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='positions',
        verbose_name='товар',
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='количество'
    )
    price = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name='цена',
    )

    class Meta:
        verbose_name = 'Товар на склад'
        verbose_name_plural = 'Товар на складе'

    def __str__(self):
        return f'{self.stock}, {self.product}, {self.quantity}, {self.price}'
