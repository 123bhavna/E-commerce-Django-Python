from django.db.models import Count,Avg
from django.shortcuts import render, redirect , get_object_or_404
from django.views import View
from . models import Product, Cart, ProductReview, Wishlist
from . forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from . forms import LoginForm, ReviewAdd
from .models import Customer
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.contrib import messages

import logging

# Create your views here.

# def home(request):
#     return render(request,"app/index.html")

class ProductView(View):
    def get(self, request):
        books = Product.objects.filter(category='BK')
        accessory = Product.objects.filter(category='AR')
        merchandise = Product.objects.filter(category='MC')
        stationary = Product.objects.filter(category='SI')
        electronics = Product.objects.filter(category='EC')
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/index.html',
        {'books':books, 'accessory':accessory,'merchandise':merchandise,'stationary':stationary,'electronics':electronics,'totalitem': totalitem,'wishitem': wishitem})

# class CartView(View):
#     def get(self,request):
#         return render(request,"app/cart.html",locals())
#     totalitem = 0
#     if request.user.is_authenticated:
#         totalitem = len(Cart.objects.filter(user=request.user))
#     return render(request,"app/index.html",locals())

# class CartView(View):
#     def get(self,request):
#         return render(request,"app/cart.html",locals())
    
    
class AccountView(View):
    def get(self,request):
        return render(request,"app/account.html",locals())
 
# class AccountView(View):
#     def get(self,request):
#         return render(request,"app/account.html",locals())



class AboutView(View):
    def get(self,request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,"app/about.html",locals())
    
class reviewsuccessView(View):
    def get(self,request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,"app/reviewsuccess.html",locals())

class ProductDetail(View):
    def get(self,request,pk):
        product= Product.objects.get(pk=pk)
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,"app/productdetail.html",locals())
    
# book detail 
@method_decorator(login_required, name='dispatch')
class ProductDetail1(View):
    def get(self, request, pk):
        product= Product.objects.get(pk=pk)
        products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
        reviewForm = ReviewAdd()
        
        # check
        canAdd=True
        reviewCheck=ProductReview.objects.filter(user=request.user,product=product).count()
        if request.user.is_authenticated:
            if reviewCheck > 0:
                canAdd=False
        # end
        
        # fetch review
        reviews=ProductReview.objects.filter(product=product)
        # end
        
        # fetch average rating for reviews
        avg_reviews=ProductReview.objects.filter(product=product).aggregate(avg_rating=Avg('review_rating'))
        # end
        
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,"app/productdetail1.html",locals())

#accessories
@method_decorator(login_required, name='dispatch')
class ProductDetail2(View):
    def get(self, request, pk):
        product= Product.objects.get(pk=pk)
        products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
        
        reviewForm = ReviewAdd()
        
        # check
        canAdd=True
        reviewCheck=ProductReview.objects.filter(user=request.user,product=product).count()
        if request.user.is_authenticated:
            if reviewCheck > 0:
                canAdd=False
        # end
        
        # fetch review
        reviews=ProductReview.objects.filter(product=product)
        # end
        
        # fetch average rating for reviews
        avg_reviews=ProductReview.objects.filter(product=product).aggregate(avg_rating=Avg('review_rating'))
        # end
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,"app/productdetail2.html",locals())


@method_decorator(login_required, name='dispatch')
class ProductDetail3(View):
    def get(self, request, pk):
        product= Product.objects.get(pk=pk)
        products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
        reviewForm = ReviewAdd()
        
        # check
        canAdd=True
        reviewCheck=ProductReview.objects.filter(user=request.user,product=product).count()
        if request.user.is_authenticated:
            if reviewCheck > 0:
                canAdd=False
        # end
        
        # fetch review
        reviews=ProductReview.objects.filter(product=product)
        # end
        
        # fetch average rating for reviews
        avg_reviews=ProductReview.objects.filter(product=product).aggregate(avg_rating=Avg('review_rating'))
        # end
        
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:   
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,"app/productdetail3.html",locals())   
    
@method_decorator(login_required, name='dispatch')
class ProductDetail4(View):
    def get(self, request, pk):
        product= Product.objects.get(pk=pk)
        products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
        reviewForm = ReviewAdd()
        
        # check
        canAdd=True
        reviewCheck=ProductReview.objects.filter(user=request.user,product=product).count()
        if request.user.is_authenticated:
            if reviewCheck > 0:
                canAdd=False
        # end
        
        # fetch review
        reviews=ProductReview.objects.filter(product=product)
        # end
        
        # fetch average rating for reviews
        avg_reviews=ProductReview.objects.filter(product=product).aggregate(avg_rating=Avg('review_rating'))
        # end
        
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,"app/productdetail4.html",locals())
    
@method_decorator(login_required, name='dispatch')
class ProductDetail5(View):
    def get(self, request, pk):
        product= Product.objects.get(pk=pk)
        products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
        reviewForm = ReviewAdd()
        
        # check
        canAdd=True
        reviewCheck=ProductReview.objects.filter(user=request.user,product=product).count()
        if request.user.is_authenticated:
            if reviewCheck > 0:
                canAdd=False
        # end
        
        # fetch review
        reviews=ProductReview.objects.filter(product=product)
        # end
        
        # fetch average rating for reviews
        avg_reviews=ProductReview.objects.filter(product=product).aggregate(avg_rating=Avg('review_rating'))
        # end
        
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,"app/productdetail4.html",locals())   
    
# women detail
@method_decorator(login_required, name='dispatch')
class ProductDetail6(View):
    def get(self, request, pk):
        product= Product.objects.get(pk=pk)
        products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
        reviewForm = ReviewAdd()
        
        # check
        canAdd=True
        reviewCheck=ProductReview.objects.filter(user=request.user,product=product).count()
        if request.user.is_authenticated:
            if reviewCheck > 0:
                canAdd=False
        # end
        
        # fetch review
        reviews=ProductReview.objects.filter(product=product)
        # end
        
        # fetch average rating for reviews
        avg_reviews=ProductReview.objects.filter(product=product).aggregate(avg_rating=Avg('review_rating'))
        # end
        
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,"app/productdetail6.html",locals())     

class CategoryView(View):
    def get(self,request,val):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))


        product= Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())

# men
def merchandise(request, data=None):
    totalitem = 0
    wishitem = 0
    
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))    
    if data == None:
        merchandise = Product.objects.filter(category='MC')
    elif data == 'tshirt' or data == 'hoodie':
        merchandise = Product.objects.filter(category='MC').filter(brand=data)
    elif data == 'below':
        merchandise = Product.objects.filter(category='MC').filter(discounted_price__lt=500)
    elif data == 'above':
        merchandise = Product.objects.filter(category='MC').filter(discounted_price__gt=500)
    return render(request, 'app/merchandise.html', {'merchandise': merchandise, 'totalitem': totalitem,'wishitem': wishitem})

# Other functions should also have consistent indentation.
# books
def books(request, data=None):
    totalitem = 0
    wishitem = 0

    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

    if data == None:
        books = Product.objects.filter(category='BK')
    elif data == 'below':
        books = Product.objects.filter(category='BK').filter(discounted_price__lt=500)
    elif data == 'above':
        books = Product.objects.filter(category='BK').filter(discounted_price__gt=500)
    
    return render(request, 'app/books.html', {'books': books, 'totalitem': totalitem,'wishitem': wishitem})


# accessory
def accessory(request, data=None):
    totalitem = 0
    wishitem = 0

    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

    if data == None:
        accessory = Product.objects.filter(category='AR')
    elif data == 'Bag' or data == 'Cover':
        accessory = Product.objects.filter(category='AR').filter(brand=data)
    elif data == 'below':
        accessory = Product.objects.filter(category='AR').filter(discounted_price__lt=500)
    elif data == 'above':
        accessory = Product.objects.filter(category='AR').filter(discounted_price__gt=500)
    
    return render(request, 'app/accessory.html', {'accessory': accessory, 'totalitem': totalitem,'wishitem': wishitem})


# stationary
def stationary(request, data=None):
    totalitem = 0
    wishitem = 0

    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

    if data == None:
        stationary = Product.objects.filter(category='SI')
    elif data == 'Diary' or data == 'Pen' or data == 'Calendar':
        stationary = Product.objects.filter(category='SI').filter(brand=data)
    elif data == 'below':
        stationary = Product.objects.filter(category='SI').filter(discounted_price__lt=500)
    elif data == 'above':
        stationary = Product.objects.filter(category='SI').filter(discounted_price__gt=500)
    
    return render(request, 'app/stationary.html', {'stationary': stationary, 'totalitem': totalitem,'wishitem': wishitem})


# electronics
def electronics(request, data=None):
    totalitem = 0
    wishitem = 0

    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

         
    if data == None:
        electronics = Product.objects.filter(category='EC')
    elif data == 'Mouse' or data == 'Keyboard' or data == 'Camera' or data == 'Headphones' or data == 'USB Cable':
        electronics = Product.objects.filter(category='EC').filter(brand=data)
    elif data == 'below':
        electronics = Product.objects.filter(category='EC').filter(discounted_price__lt=500)
    elif data == 'above':
        electronics = Product.objects.filter(category='EC').filter(discounted_price__gt=500)
    
    return render(request, 'app/electronics.html', {'electronics': electronics, 'totalitem': totalitem,'wishitem': wishitem})


# Women
def Women(request, data=None):
    totalitem = 0
    wishitem = 0

    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))


    if data == None:
        Women = Product.objects.filter(category='WM')
    elif data == 'tshirt' or data == 'hoodie':
        Women = Product.objects.filter(category='WM').filter(brand=data)
    elif data == 'below':
        Women = Product.objects.filter(category='WM').filter(discounted_price__lt=500)
    elif data == 'above':
        Women = Product.objects.filter(category='WM').filter(discounted_price__gt=500)
    
    return render(request, 'app/Women.html', {'Women': Women, 'totalitem': totalitem,'wishitem': wishitem})


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        totalitem = 0
        wishitem = 0

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))


        return render(request, "app/customerregistration.html", locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Registered Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        
        return redirect("login")


class ProfileView(View):
    def get(self, request):
        return render(request, "app/profile.html", locals())

    def post(self, request):
        return render(request, "app/profile.html", locals())
    

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        totalitem = 0
        wishitem = 0

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))


        return render(request, 'app/profile.html', locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user, name=name, locality=locality, city=city, mobile=mobile, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Profile Save Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        
        return render(request, 'app/profile.html', locals())


@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    totalitem = 0
    wishitem = 0

    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

    
    return render(request, 'app/address.html', locals())


class updateAddress(View):   
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        totalitem = 0
        wishitem = 0

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))

        
        return render(request, 'app/updateAddress.html', locals())

    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, "Congratulation Profile Updated Successfully")
        else:
            messages.warning("Invalid Input data")
 

# @login_required
# def add_to_cart(request):
#     user=request.user
#     product_id=request.GET.get('prod_id')
#     product = Product.objects.get(id=product_id)
#     Cart(user=user,product=product).save()
#     return redirect('/cart')
@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)

    # Check if the product is already in the cart
    if Cart.objects.filter(user=user, product=product).exists():
        messages.warning(request, 'This product is already in your cart.')
    else:
        # If not in the cart, add it
        Cart(user=user, product=product).save()
        messages.success(request, 'Product added to cart successfully.')

    return redirect('/cart')


@login_required
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
        if  amount > 1000:
            totalamount = amount 
        else:
            totalamount = amount + 40
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

    return render(request, 'app/addtocart.html',locals())
 
 
@method_decorator(login_required,name='dispatch')
class checkout(View):
    def get(self,request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))

        user=request.user
        add=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
            if  famount > 1000:
                totalamount = famount 
            else:
                totalamount = famount + 40
        
        return render(request,"app/checkout.html",locals())
    
   
 
@login_required
def plus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        if  amount > 1000:
            totalamount = amount 
        else:
            totalamount = amount + 40
        # print(prod_id)
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
    
def minus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        if  amount > 1000:
            totalamount = amount 
        else:
            totalamount = amount + 40 
        # print(prod_id)
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def remove_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        if  amount > 1000:
            totalamount = amount 
        else:
            totalamount = amount + 40
        # print(prod_id)
        data={
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    from django.http import Http404

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        try:
            c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            c.delete()
        except Cart.DoesNotExist:
            raise Http404("Cart does not exist")
        user = request.user
        cart = Cart.objects.filter(user=user)
    return redirect('/cart')

 
 
#  remove whislist
def remove_wishlist(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        wishlist = Wishlist.objects.get(Q(product=prod_id) & Q(user=request.user))
        wishlist.delete()
        user = request.user
        wishlist = Wishlist.objects.filter(user=user)
    return redirect('/wishlist')
@method_decorator(login_required,name='dispatch')
class FAQsView(View):
    def get(self,request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))

        return render(request,'app/FAQs.html',locals())
    
@method_decorator(login_required,name='dispatch')    
class termsView(View):
    def get(self,request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))

        return render(request,'app/terms.html',locals())
    
    from django.shortcuts import redirect


@login_required    
def search(request):
    query = request.GET['search']
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

    product = Product.objects.filter(Q(title__icontains=query))
    return render(request,"app/search.html",locals())
    
    

# sava review
def save_review(request, pid):
    product = Product.objects.get(pk=pid)
    user = request.user
    review = ProductReview.objects.create(
        user=user,
        product=product,
        review_text=request.POST['review_text'],
        review_rating=request.POST['review_rating'],
        )
    
    data={
        'user':user.username,
        'review_text':request.POST['review_text'],
        'review_rating':request.POST['review_rating']
    }
    # fetch average rating for reviews
    avg_reviews=ProductReview.objects.filter(product=product).aggregate(avg_rating=Avg('review_rating'))
    # end
    # return JsonResponse({'bool': True,'data':data,'avg_reviews':avg_reviews})
    # messages.success(request, "Congratulations! User Registered Successfully")
    return redirect('/reviewsuccess')
    
      
    

# def add_to_wishlist(request):
#     if request.method == "POST":
#         print(request.POST)
#     user=request.user
#     product_id=request.GET.get('prod_id')
#     product = Product.objects.get(id=product_id)
#     Wishlist(user=user,product=product).save()
#     return redirect('/wishlist')
@login_required
def add_to_wishlist(request):
    if request.method == "POST":
        print(request.POST)

    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)

    # Check if the product is already in the wishlist
    if Wishlist.objects.filter(user=user, product=product).exists():
        messages.warning(request, 'This product is already in your wishlist.')
    else:
        # If not in the wishlist, add it
        Wishlist(user=user, product=product).save()
        messages.success(request, 'Product added to wishlist successfully.')

    return redirect('/wishlist')


 

 
@login_required
def show_wishlist(request):
    user_id = request.user.id
    wishitem = 0
    wishlist = []

    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user=request.user)
        wishitem = len(wishlist)

    return render(request, "app/addtowishlist.html", {'wishlist': wishlist, 'wishitem': wishitem})


def remove_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        print("Removing item with ID:", prod_id)

        wishlist_item = Wishlist.objects.filter(Q(product=prod_id) & Q(user=request.user)).first()

        if wishlist_item:
            wishlist_item.delete()
            return JsonResponse({'message': 'Item removed successfully'})

        return JsonResponse({'error': 'Item not found in wishlist'})
    return redirect('/wishlist')

@login_required
def remove_from_wishlist(request, product_id):
      
    try:
        wishlist_item = Wishlist.objects.get(user=request.user, product_id=product_id)
        wishlist_item.delete()
        return JsonResponse({'message': 'Item removed successfully'})
    except Wishlist.DoesNotExist:
        return JsonResponse({'error': 'Item not found in wishlist'})
        
    
    
    