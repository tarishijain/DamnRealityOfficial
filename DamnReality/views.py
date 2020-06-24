from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Product, Category, Order, Contact
from .forms_order import OrderForm
# Create your views here.

def crud(request):
    
    products = Product.objects.all()
    categories = Category.objects.all()
    params = {'products': products, 'categories' : categories}

    return render(request, 'DamnReality/index.html', params)
    
def showcategory(request, cat):
    
    categories = Category.objects.all()

    cats = Category.objects.get(name=cat)

    products = Product.objects.filter(category=cats).values()

    params = {'products' : products, 'category' : cat, 'categories' : categories}

    return render(request, 'DamnReality/category.html', params)

def showproduct(request, product_id):

    product = Product.objects.get(id=product_id)
    related = Product.objects.exclude(id=product_id).values 

    params = {'product' : product, 'related': related}

    return render(request, 'DamnReality/product.html', params)

def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid(): # All validation rules pass
            order = form.save(commit=False)
            order.user = request.user
            order.status = 'PLACED'
            order.order_id = "OrderId" + str(form.cleaned_data.get('order_id'))
            order.save()
            params = {'submitted' : '1'}
            return render(request, 'DamnReality/order.html', params)    
    else:
        form = OrderForm()

    return render(request, 'DamnReality/order.html', {
        'form': form, 'submitted' : '0',
    })           


def about(request):
        return render(request, 'DamnReality/about.html')


def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'DamnReality/contact.html', {'thank': thank})


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'DamnReality/tracker.html')
