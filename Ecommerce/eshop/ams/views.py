from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Contact,Order, OrderUpdate
from math import ceil
import json
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request,'You entered wrong info')
            return redirect('/')
    
        user = authenticate(username=username,password=password)
        if user == None:
            messages.info(request,'You entered wrong info')
            return redirect('/')
        else:
            login(request,user)
            return redirect('/home')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username Already Exist.")
            return redirect('/register')
        

        user = User.objects.create(first_name=first_name,last_name=last_name,username=username)
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully.")
        return redirect('/register')
    
    return render(request,'register.html')

def logout_page(request):
    logout(request)
    return redirect('/')








@login_required(login_url='/')
def home(request):
    # product=Product.objects.all()
    # n=len(product)
    # if n%2==0:
    #     nslides=n//4
    # else:
    #     nslides=(n//4)+1
    # allprods=[[product,range(1,nslides)],[product,range(1,nslides)]]
    # # param={'range':range(1,nslides),'nslides':nslides,'product':product}
    # params={'allprod':allprods}
    # return render(request,'home.html',params)


    # products= Product.objects.all()
    # allProds=[]
    # catprods= Product.objects.values('category', 'id')
    # cats= {item["category"] for item in catprods}
    # for cat in cats:
    #     prod=Product.objects.filter(category=cat)
    #     n = len(prod)
    #     nSlides = n // 4 + ceil((n / 4) - (n // 4))
    #     allProds.append([prod, range(1, nSlides), nSlides])

    products = Product.objects.all()
    products_by_category = {}

    for product in products:
        category = product.category
        if category not in products_by_category:
            products_by_category[category] = []
        products_by_category[category].append(product)

    allProds = []

    for category, product in products_by_category.items():
        n = len(product)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([product, range(1, nSlides), nSlides])        

    params={'allProds':allProds }
    return render(request,"home.html", params)

@login_required(login_url='/')
def about(request):
    return render(request,'about.html')

@login_required(login_url='/')
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request,'contact.html')

@login_required(login_url='/')
def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'tracker.html')

@login_required(login_url='/')
def search(request):
    return render(request,'search.html')

@login_required(login_url='/login')
def productView(request,myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request,'prodview.html',{'product':product[0]})

@login_required(login_url='/')
def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id': id})
    return render(request, 'checkout.html')