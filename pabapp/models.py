from django.db import models

class CategoryGroup(models.Model):
    category_group_name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.category_group_name}"

class Category(models.Model):
    category_name = models.CharField(max_length=128)
    category_group = models.ForeignKey(CategoryGroup, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.category_name} - {self.category_group}"

class Account(models.Model):
    account_name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.account_name}"

class Currency(models.Model):
    currency_name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.currency_name}"

class ValueType(models.Model):
    value_type_name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.value_type_name}"

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    transaction_date = models.DateField()
    transaction_description = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    value_type = models.ForeignKey(ValueType, on_delete=models.PROTECT)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    value = models.DecimalField(max_digits=15, decimal_places=2)
