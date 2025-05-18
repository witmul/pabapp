import csv

from django.shortcuts import render, redirect, get_object_or_404
from .models import CategoryGroup, Category, Account, Currency, ValueType, Transaction
from .forms import CategoryGroupForm, CategoryForm, AccountForm, CurrencyForm, ValueTypeForm, TransactionForm, CSVImportForm

#  ██████╗ █████╗ ████████╗███████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗     ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗
# ██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔════╝ ██╔═══██╗██╔══██╗╚██╗ ██╔╝    ██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗
# ██║     ███████║   ██║   █████╗  ██║  ███╗██║   ██║██████╔╝ ╚████╔╝     ██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝
# ██║     ██╔══██║   ██║   ██╔══╝  ██║   ██║██║   ██║██╔══██╗  ╚██╔╝      ██║   ██║██╔══██╗██║   ██║██║   ██║██╔═══╝
# ╚██████╗██║  ██║   ██║   ███████╗╚██████╔╝╚██████╔╝██║  ██║   ██║       ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║
#  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝

def create_category_group(request):
    if request.method == "POST":
        form = CategoryGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category_group")
    else:
        form = CategoryGroupForm()

    items = CategoryGroup.objects.all()
    return render(request, "pabapp/category_group_list.html", {"form": form, "items": items})

def update_category_group(request, pk):
    item = get_object_or_404(CategoryGroup, pk=pk)
    if request.method == "POST":
        form = CategoryGroupForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("category_group")
    else:
        form = CategoryGroupForm(instance=item)

    return render(
        request, "pabapp/update_page.html", {"form": form, "items": item, "page_name": "category_group"}
    )


def delete_category_group(request, pk):
    item = get_object_or_404(CategoryGroup, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect("category_group")

    return render(
        request,
        "pabapp/delete_page.html",
        {"item": item.category_group_name, "page_name": "category_group"},
    )

#  ██████╗ █████╗ ████████╗███████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗
# ██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔════╝ ██╔═══██╗██╔══██╗╚██╗ ██╔╝
# ██║     ███████║   ██║   █████╗  ██║  ███╗██║   ██║██████╔╝ ╚████╔╝
# ██║     ██╔══██║   ██║   ██╔══╝  ██║   ██║██║   ██║██╔══██╗  ╚██╔╝
# ╚██████╗██║  ██║   ██║   ███████╗╚██████╔╝╚██████╔╝██║  ██║   ██║
#  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝

def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category")
    else:
        form = CategoryForm()

    items = Category.objects.all()
    return render(request, "pabapp/category_list.html", {"form": form, "items": items})


def update_category(request, pk):
    item = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("category")
    else:
        form = CategoryForm(instance=item)

    return render(
        request, "pabapp/update_page.html", {"form": form, "items": item, "page_name": "category"}
    )

def delete_category(request, pk):
    item = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect("category")

    return render(
        request, "pabapp/delete_page.html", {"item": item.category_name, "page_name": "category"}
    )

#  █████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗
# ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝
# ███████║██║     ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║
# ██╔══██║██║     ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║
# ██║  ██║╚██████╗╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║
# ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝


def create_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account")
    else:
        form = AccountForm()

    items = Account.objects.all()
    return render(request, "pabapp/account_list.html", {"form": form, "items": items})


def update_account(request, pk):
    item = get_object_or_404(Account, pk=pk)
    if request.method == "POST":
        form = AccountForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("account")
    else:
        form = AccountForm(instance=item)

    return render(
        request, "pabapp/update_page.html", {"form": form, "items": item, "page_name": "account"}
    )


def delete_account(request, pk):
    item = get_object_or_404(Account, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect("account")

    return render(
        request, "pabapp/delete_page.html", {"item": item.account_name, "page_name": "account"}
    )

#  ██████╗██╗   ██╗██████╗ ██████╗ ███████╗███╗   ██╗ ██████╗██╗   ██╗
# ██╔════╝██║   ██║██╔══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝╚██╗ ██╔╝
# ██║     ██║   ██║██████╔╝██████╔╝█████╗  ██╔██╗ ██║██║      ╚████╔╝
# ██║     ██║   ██║██╔══██╗██╔══██╗██╔══╝  ██║╚██╗██║██║       ╚██╔╝
# ╚██████╗╚██████╔╝██║  ██║██║  ██║███████╗██║ ╚████║╚██████╗   ██║
#  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝   ╚═╝


def create_currency(request):
    if request.method == "POST":
        form = CurrencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("currency")
    else:
        form = CurrencyForm()

    items = Currency.objects.all()
    return render(request, "pabapp/currency_list.html", {"form": form, "items": items})


def update_currency(request, pk):
    item = get_object_or_404(Currency, pk=pk)
    if request.method == "POST":
        form = CurrencyForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("currency")
    else:
        form = CurrencyForm(instance=item)

    return render(
        request, "pabapp/update_page.html", {"form": form, "items": item, "page_name": "currency"}
    )


def delete_currency(request, pk):
    item = get_object_or_404(Currency, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect("currency")

    return render(
        request, "pabapp/delete_page.html", {"item": item.currency_name, "page_name": "currency"}
    )

# ██╗   ██╗ █████╗ ██╗     ██╗   ██╗███████╗     ████████╗██╗   ██╗██████╗ ███████╗
# ██║   ██║██╔══██╗██║     ██║   ██║██╔════╝     ╚══██╔══╝╚██╗ ██╔╝██╔══██╗██╔════╝
# ██║   ██║███████║██║     ██║   ██║█████╗          ██║    ╚████╔╝ ██████╔╝█████╗
# ╚██╗ ██╔╝██╔══██║██║     ██║   ██║██╔══╝          ██║     ╚██╔╝  ██╔═══╝ ██╔══╝
#  ╚████╔╝ ██║  ██║███████╗╚██████╔╝███████╗███████╗██║      ██║   ██║     ███████╗
#   ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝      ╚═╝   ╚═╝     ╚══════╝


def create_value_type(request):
    if request.method == "POST":
        form = ValueTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("value_type")
    else:
        form = ValueTypeForm()

    items = ValueType.objects.all()
    return render(request, "pabapp/value_type_list.html", {"form": form, "items": items})


def update_value_type(request, pk):
    item = get_object_or_404(ValueType, pk=pk)
    if request.method == "POST":
        form = ValueTypeForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("value_type")
    else:
        form = ValueTypeForm(instance=item)

    return render(
        request, "pabapp/update_page.html", {"form": form, "items": item, "page_name": "value_type"}
    )


def delete_value_type(request, pk):
    item = get_object_or_404(ValueType, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect("value_type")

    return render(
        request,
        "pabapp/delete_page.html",
        {"item": item.value_type_name, "page_name": "value_type"},
    )

# ████████╗██████╗  █████╗ ███╗   ██╗███████╗ █████╗  ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗
# ╚══██╔══╝██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔══██╗██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
#    ██║   ██████╔╝███████║██╔██╗ ██║███████╗███████║██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗
#    ██║   ██╔══██╗██╔══██║██║╚██╗██║╚════██║██╔══██║██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║
#    ██║   ██║  ██║██║  ██║██║ ╚████║███████║██║  ██║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║
#    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝


def create_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("transaction")
    else:
        form = TransactionForm()

    items = Transaction.objects.all()
    return render(request, "pabapp/transaction_list.html", {"form": form, "items": items})


def update_transaction(request, pk):
    item = get_object_or_404(Transaction, pk=pk)
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("transaction")
    else:
        form = TransactionForm(instance=item)

    return render(
        request, "pabapp/update_page.html", {"form": form, "items": item, "page_name": "transaction"}
    )


def delete_transaction(request, pk):
    item = get_object_or_404(Transaction, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect("transaction")

    return render(
        request,
        "pabapp/delete_page.html",
        {"item": item.pk, "page_name": "transaction"},
    )


def import_csv(request):
    if request.method == "POST":
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES["csv_file"].read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(csv_file)
            
            for row in csv_reader:
                # breakpoint()
                Transaction.objects.create(
                    # To make it work, i need to pass actual Account instance, not just string
                    account = Account.objects.get(account_name=row['account_name']),
                    transaction_date = row['date'],
                    transaction_description = row['description'], 
                    category = Category.objects.get(category_name = row['category_name']),
                    value_type = ValueType.objects.get(value_type_name = row['value_type']),
                    currency = Currency.objects.get(currency_name = row['currency']),
                    value = row['value'],
                )
            return redirect('transaction')  # Redirect to a success page
    else:
        form = CSVImportForm()

    return render(request, 'pabapp/import_csv.html', {'form': form})