from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from django.db.models import Q
from app.models import Product, Customers, Specific, Specific_value
from app.forms import  CustomerModelForm

# Create your views here.


def index(request):
    products = Product.objects.all()
    search_query = request.GET.get('search', '')
    paginator = Paginator(products, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if search_query:
        search = Product.objects.filter(Q(name__icontains=search_query) | Q(email__contains=search_query))
    else:
        search = Product.objects.all()
    context = {
        'page_obj': page_obj,
        'search': search,
    }
    return render(request, 'app/index.html', context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    specifics = Specific.objects.all()
    specific_values = Specific_value.objects.all()
    context = {
        'product': product,
        'specifics': specifics,
        'specific_values': specific_values,

    }
    return render(request, 'app/product-details.html', context)

def customer(request):
    customer = Customers.objects.all()
    context = {
        'customer': customer,
        }
    return render(request, 'app/customers.html', context)



def customer_detail(request):
    customer_id = request.GET.get('id')
    customer = Customers.objects.filter(id=customer_id).first()
    context = {
        'customer': customer,
         }
    return render(request, 'app/customer-details.html', context)

def delete_customer(request, customer_id):
    customer = get_object_or_404(Customers, id=customer_id)
    if customer:
        customer.delete()
        return redirect('index')

    context = {
        'customer': customer,
    }
    return render('app/customers.html', context)

def edit_customer(request, pk):
    customer = Customers.objects.get(id=pk)
    form = CustomerModelForm(instance=customer)
    if request.method == 'POST':
        form = CustomerModelForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('detail', customer.id)

    context = {
        'form': form,
        'customer': customer
    }
    return render(request, 'app/update-customer.html', context)

def add_customer(request):
    if request.method == 'POST':
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer')

    else:
        form = CustomerModelForm()
    context = {
        'form': form
    }
    return render(request, 'app/index.html', context)