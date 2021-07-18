from django.db import models


class Deals(models.Model):
    customer = models.CharField('Логин покупателя', max_length=255)
    item = models.CharField('Наименование товара', max_length=255)
    total = models.PositiveBigIntegerField('Сумма сделки')
    quantity = models.IntegerField('Количество товара, шт', )
    date = models.DateTimeField('Дата и время регистрации сделки')
