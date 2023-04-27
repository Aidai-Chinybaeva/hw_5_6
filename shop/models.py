from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def str(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def str(self):
        return self.name


class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Кол-во товара')

    def str(self):
        return self.item
