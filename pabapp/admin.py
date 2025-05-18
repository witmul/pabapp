from django.contrib import admin
from pabapp.models import CategoryGroup, Category, Account, Currency, ValueType, Transaction


admin.site.register(CategoryGroup)
admin.site.register(Category)
admin.site.register(Account)
admin.site.register(Currency)
admin.site.register(ValueType)
admin.site.register(Transaction)