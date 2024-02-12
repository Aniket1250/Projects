import json
from django.shortcuts import render,redirect
from .models import Product,Orders,Contact
from django.http import HttpResponse
# Create your views here.
def home(request):
    if request.method == 'GET':
        # Retrieve the cart data from the request
        cart_data = request.POST.get('data')
        print('Received Cart Data:',cart_data)
        products = Product.objects.all()  # Replace with your actual queryset
        print(f'{products}')
        return render(request, 'home.html', {'products': products})

def category(request,name):
    if request.method == 'GET':
        # Retrieve the cart data from the request
        cart_data = Product.objects.filter(category=name)
        print('Received Cart Data:',cart_data)
        # products = Product.objects.all()  # Replace with your actual queryset
        return render(request, 'category.html', {'products': cart_data})    

def about(request):
    return render(request,'about.html')

def stock(request):
    dt=Product.objects.all()
    data={'data':dt}
    return render(request,'stock.html',data)

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request,'contact.html')

def add(request):
    if request.method=='GET':
        context = {'success': False }
        return render(request,'add.html',context)
    else:
        
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        price=request.POST.get('price')
        category=request.POST.get('category')
        image=request.FILES['image'] 

        data=Product.objects.create(name=name,desc=desc,price=price,category=category,image=image)
        data.save()
        context = {'success': True }
        return render(request,'add.html',context)
    

def checkout(request):
    if request.method == 'GET':
        context = {'success': False }
        # Retrieve the cart data from the request
        cart_data = request.POST.get('data')
        print('Received Cart Data:',cart_data)
        return render(request,'checkout.html',context)  
      
    cart_data = ""  # Provide an initial assignment to avoid UnboundLocalError
    
    if request.method == 'POST':
        # Retrieve data sent from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        payment_method = request.POST.get('paymentMethod')

        # Fetch cart data from the session (you may need to adapt this based on how your form is structured)
        cart_data = request.POST.get('data')
        print(cart_data)
        cartdt = json.loads(cart_data)  # Use json.loads to convert the JSON string to a dictionary
        print(cartdt)
        # Process each item in the cart
        for product_id, item_data in cartdt.items():
            quantity = item_data['quantity']
            product = Product.objects.get(pk=product_id)

            # Ensure there is enough stock before processing the order
            if product.stock >= quantity:
                # Decrease the product quantity in stock
                product.stock -= quantity
                product.save()
            else:
                return HttpResponse('You dont have stock')
                # If there is not enough stock, handle the error (e.g., return an error response)

        # Perform the database insertion after updating product stocks
        order = Orders(
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            zip_code=zip_code,
            cart_data=cartdt,
            payment_method=payment_method,
        )
        order.save()

        context = {'success': True}
        # Redirect to a success page or perform other actions
        return render(request, 'checkout.html', context)

    context = {'success': False}
    return render(request, 'checkout.html', context)


def about(request):
    return render(request,'about.html')
