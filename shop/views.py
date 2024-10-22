from django.shortcuts import render, redirect
from .models import Product, Order,ContactMessage
from django.contrib import messages

def index(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'shop/templates/home.html', {'products': products})

def create_order(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        name = request.POST.get('name')
        address = request.POST.get('address')
        quantity = request.POST.get('quantity')
        
        # Create an Order
        order = Order.objects.create(name=name, address=address, product=product, quantity=quantity)
        messages.success(request, 'Order successfully submitted! We will contact you soon.')
        return redirect('home')  # Redirect to home after submitting
    else:
        product = Product.objects.get(id=product_id)
        return render(request, 'shop/templates/create_order.html', {'product': product})
    
def contact_view(request):
    success_message = None

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the data to the database
        contact_message = ContactMessage(name=name, email=email, message=message)
        contact_message.save()

        success_message = 'Your message has been successfully submitted.'

    return render(request, 'shop/templates/contact.html', {'success_message': success_message})

def about_view(request):
    return render(request, 'shop/templates/about.html')