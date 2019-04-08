from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    addres = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name',)

class Storage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date_storage = models.DateField()

    def __str__(self):
        return self.product.name

    @property
    def price(self):
        return self.product.price

    @property
    def total(self):
        return self.product.price * self.amount


class Sell(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def update_storage(self):
        pk = self.products.id
        item_amout = Product.objects.get(id=pk).amount
        new_amount = item_amout - self.amount
        if item_amout > 0 and new_amount > 0:
            Product.objects.filter(id=pk).update(amount=new_amount)

    def save(self, *args, **kwargs):
        self.update_storage()
        return super().save(*args, **kwargs)


class Cart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sell_itens = models.ForeignKey(Sell, on_delete=models.CASCADE, related_name="sell_itens")

    # def empty_cart(self, items):
    #     validate = False
    #     if items.count != 0:
    #         validate = True
    #     return validate


    # @property
    # def total(self):
    #     sum = 0
    #     for item in self.buy_itens:
    #         sum += item.products.price
    #     return sum


    # def save(self, *args, **kwargs):
    #     if self.empty_cart(self.buy_itens):
    #         return super().save(*args, **kwargs)