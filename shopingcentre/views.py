from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from cart.models import Cart, CartItem
from cart.views import cart

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='shopingcentre:login')
def index(request):
    profile = Profile.objects.get(user_id=request.user)
    

    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = str(profile.phone)
    if phone_number.startswith('0'):
        phone_number = '254' + phone_number[1:]  # Replace leading '0' with '254' for Kenyan numbers
    amount=5000
    account_reference = 'tedShop'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push(request):
        data = request.body
        return HttpResponse("STK Push in Django👋")
@login_required(login_url='shopingcentre:login')
def update_profile(request):
    if request.user.is_authenticated:
        current_user= Profile.objects.get(user_id=request.user.id)
        user_form=UserInfoForm(request.POST or None, instance=current_user)
        
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile info is updated successfully')
            return redirect('shopingcentre:home')
        return render(request, 'update_profile.html',{'user_form':user_form})
    else:
        messages.error(request, 'Your are not logged in')
        return redirect('shopingcentre:login')
@login_required(login_url='shopingcentre:login')
def update_password(request):
    if request.user.is_authenticated:
        current_user= request.user
        if request.method== 'POST':
            form=ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password changed successfully')
                return redirect('shopingcentre:login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('shopingcentre:login')
        else:
            form=ChangePasswordForm(current_user)
            return render(request, 'update_password.html', {'form':form})
    else:
        
        return redirect('shopingcentre:login')

@login_required(login_url='shopingcentre:login')
def update_user(request):
    
    if request.user.is_authenticated:
        current_user= User.objects.get(id=request.user.id)
        user_form=UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, 'Your profile is updated successfully')
            return redirect('shopingcentre:home')
        return render(request, 'update_user.html',{'user_form':user_form})
    else:
        messages.error(request, 'Your are not logged in')
        return redirect('shopingcentre:login')
        
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'login.html')
def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            email=form.cleaned_data['email']
            user=authenticate(username=username, password=password, email=email)
            login(request, user)
            messages.success(request, 'Account was created successfully')
            return redirect('shopingcentre:update_profile')
    else:
        form=SignUpForm()
    
    return render(request, 'signup.html',{'form':form})

@login_required(login_url='shopingcentre:login')
def logout_user(request):
    logout(request)
    return redirect('/')

def home(request):
    return render(request, 'landing_page.html')


def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='shopingcentre:login')
def shop(request):
    products = Product.objects.all()
    context={
        'products':products
    }
    return render(request, 'shop.html', context)

@login_required(login_url='shopingcentre:login')
def product(request, pk):
    product = Product.objects.get(id=pk)
    context={
        'product':product
    }
    return render(request, 'product.html', context)

@login_required(login_url='shopingcentre:login')
def category(request, foo):
    foo= foo.replace('-', ' ')
    # grab the category from the url\\
    try:
        # lookup the category
        category=Category.objects.get(name=foo)
        # get all products in that category
        products=Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})
    except:
        messages.success(request, 'Category does not exist')
        return redirect('/')