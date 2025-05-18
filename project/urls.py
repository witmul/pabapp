"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from pabapp.views import (
    create_category_group,
    update_category_group,
    delete_category_group,
    create_category,
    update_category,
    delete_category,
    create_account,
    update_account,
    delete_account,
    create_currency,
    update_currency,
    delete_currency,
    create_value_type,
    update_value_type,
    delete_value_type,
    create_transaction,
    update_transaction,
    delete_transaction,
    import_csv
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("category_group/", create_category_group, name="category_group"),
    path("category_group/<int:pk>/edit/", update_category_group, name="category_group_update"),
    path("category_group/<int:pk>/delete/", delete_category_group, name="category_group_delete"),
    path("category/", create_category, name="category"),
    path("category/<int:pk>/edit/", update_category, name="category_update"),
    path("category/<int:pk>/delete/", delete_category, name="category_delete"),
    path("account/", create_account, name="account"),
    path("account/<int:pk>/edit/", update_account, name="account_update"),
    path("account/<int:pk>/delete/", delete_account, name="account_delete"),
    path("currency/", create_currency, name="currency"),
    path("currency/<int:pk>/edit/", update_currency, name="currency_update"),
    path("currency/<int:pk>/delete/", delete_currency, name="currency_delete"),
    path("value_type/", create_value_type, name="value_type"),
    path("value_type/<int:pk>/edit/", update_value_type, name="value_type_update"),
    path("value_type/<int:pk>/delete/", delete_value_type, name="value_type_delete"),
    path("transaction/", create_transaction, name="transaction"),
    path("transaction/<int:pk>/edit/", update_transaction, name="transaction_update"),
    path("transaction/<int:pk>/delete/", delete_transaction, name="transaction_delete"),
    path('import_csv/', import_csv, name='import_csv')
]
