import datetime
from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    #products = Product.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'class': 'PBP C',
        'npm': '2306245491',
        'profile_picture_url': '/static/image/akun.png',
        #'products': products,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
           user = form.get_user()
           login(request, user)
           response = HttpResponseRedirect(reverse("main:show_main"))
           response.set_cookie('last_login', str(datetime.datetime.now()))
           return response
      else:
           messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get product berdasarkan id
    product = Product.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))


@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    stock = request.POST.get("stock")
    rating = request.POST.get("rating")
    user = request.user

    # Validasi data
    errors = []
    if not name:
        errors.append("Name is required.")
    if not price or not price.isdigit():
        errors.append("Price is required and must be a number.")
    if not description:
        errors.append("Description is required.")
    if not stock or not stock.isdigit():
        errors.append("Stock is required and must be a number.")
    if not rating or not rating.replace('.', '', 1).isdigit():
        errors.append("Rating is required and must be a number.")
    else:
        # Convert rating to float and validate range
        rating_value = float(rating)
        if rating_value < 1 or rating_value > 10:
            errors.append("Rating must be between 1 and 10.")

    # Jika ada error, kembalikan respons dengan pesan error
    if errors:
        return JsonResponse({"errors": errors}, status=400)

    # Simpan produk baru jika semua input valid
    new_product = Product(
        name=name, price=price,
        description=description,
        stock=stock, rating=rating_value,
        user=user
    )
    new_product.save()
    
    # Kirim respons sukses
    return JsonResponse({
        "message": "Product added successfully",
        "product": {
            "name": new_product.name,
            "price": new_product.price,
            "description": new_product.description,
            "stock": new_product.stock,
            "rating": new_product.rating,
        }
    }, status=201)