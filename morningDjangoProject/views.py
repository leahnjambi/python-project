from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Product


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def add_product(request):
    if request.method == 'POST':
        p_name = request.POST.get("jina")
        p_quantity = request.POST.get("kiasi")
        p_price = request.POST.get("bei")
        product = Product(prod_name=p_name, prod_quantity=p_quantity, prod_price=p_price)

        product.save()
        messages.success(request, 'product saved successfully')
        return redirect('add-product')
    return render(request, 'add product.html')


@login_required
def view_products(request):
    # Select all the product from the database
    products = Product.objects.all()
    # Render the template with the products
    return render(request, 'products.html', {'products': products})


@login_required
def delete_product(request, id):
    # Select the product you want to delete
    product = Product.objects.get(id=id)
    # finally delete the product
    product.delete()
    # Redirect back to products page with a success message
    messages.success(request, 'Product deleted successfully')
    return redirect('products')


@login_required
def update_product(request, id):
    # Select the product to be updated
    product = Product.objects.get(id=id)

    # Check if the form has any submitted records to receive them

    if request.method == 'POST':
        update_name = request.POST.get('jina')
        update_quantity = request.POST.get('kiasi')
        update_price = request.POST.get('bei')

        # Update the submitted product above with the received data

        product.prod_name = update_name
        product.prod_quantity = update_quantity
        product.prod_price = update_price

        # Return the updated data back to the database

        product.save()

        # Redirect back to the products page with a success message
        messages.success(request, 'Product updated successfully')
        return redirect('products')
    return render(request, 'update product.html', {'product': product})



@login_required
def payment(request, id):
    # Select the product being paid
    product = Product.objects.get(id=id)
    # Check if the form having submitted has a post method
    if request.method == 'POST':
        phone_number = request.POST.get('nambari')
        amount = request.POST.get('bei')
        # Proceed with the payment by launching mpesa STK

    return render(request, 'payment.html', {'product': product})
