from django import forms
from .models import CategoryGroup, Category, Account, Currency, ValueType, Transaction


class DateInput(forms.DateInput):
    input_type = "date"


class CategoryGroupForm(forms.ModelForm):
    class Meta:
        model = CategoryGroup
        fields = ["category_group_name"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["category_name", "category_group"]


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["account_name"]


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ["currency_name"]


class ValueTypeForm(forms.ModelForm):
    class Meta:
        model = ValueType
        fields = ["value_type_name"]


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            "account",
            "transaction_date",
            "transaction_description",
            "category",
            "value_type",
            "currency",
            "value",
        ]
        widgets = {
            "transaction_date": DateInput(),
        }


class CSVImportForm(forms.Form):
    csv_file = forms.FileField()