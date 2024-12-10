from email import message
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from http import client
from multiprocessing import Condition
from django.contrib import messages
from django.shortcuts import render,redirect
from django.test import Client
from markupsafe import escape_silent
from matplotlib.style import use
from des.models import Order, OrderItem, filter_price, product,categorie,subcategorie,color,brand,contactus,profile
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from cart .cart import Cart
import razorpay
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import cancel 



client =razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRATE))


def reg(r):
    return render(r,'regis.html')


def log(r):
    return render(r,'loigis.html')


def base(r):
    return render(r,'base.html')

def compare(r):
    return render(r,'compare.html')


from django.shortcuts import render, redirect
from .models import Review

def save_review(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        count = int(request.POST.get('stars'))  # Convert the rating value to an integer
        message = request.POST.get('message')
        review = Review(firstname=firstname, lastname=lastname, count=count, message=message)
        review.save()

        return redirect('product')  # Redirect to a success page (adjust the URL as needed)
    else:
        return render(request, 'product')  # Render the form initially

from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from .models import profile as ProfileModel  # Import the profile model as ProfileModel

def profil(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        user = User.objects.get(id=userid)  # Get the User object with the given userid
        country = request.POST.get('country')
        state = request.POST.get('state')  # Convert the rating value to an integer
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        

        # Check if a profile already exists for the user
        pro, created = ProfileModel.objects.get_or_create(user=user, defaults={'country': country, 'state': state, 'phone': phone, 'address': address})

        # If a profile already exists, update it
        if not created:
            pro.country = country
            pro.state = state
            pro.phone = phone
            pro.address = address
            pro.save()

        return redirect('/pro.html')  
    else:
        return render(request, 'userprofile.html')



def pr(r):
    return render (r,'pro.html')

def message(r):
    return render(r,'message.html')


from django.shortcuts import render, redirect
from .models import cancel 
def Cancel(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('country')
        message = request.POST.get('message')

        # Create a new Cancel object
        cancel_o = cancel(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        # Save the Cancel object to the database
        cancel_o.save()

        # Redirect to a success page (replace 'success' with the actual URL pattern)
        return redirect('/done/')

    # Render the form page (replace 'form.html' with the actual template name)
    return render(request, 'cancel.html')
 


@login_required
def done(r):
    return render(r,'done.html')



# views.py
from django.shortcuts import render
from .models import cancel

def re(request):
   
    user_reviews = cancel.objects.all()

    context = {
        'user_reviews': user_reviews,
        
    }
    return render(request, 'req.html', context)





@login_required
def track(request):
    current_user = request.user
    orders = Order.objects.filter(user=current_user)
    

    context = {
        'orders': orders,
        'user': current_user,
    }
    return render(request, 'track.html', context)

def your_order(r):
    uid=r.session.get('_auth_user_id')
    user=User.objects.get(id = uid)
    order=OrderItem.objects.filter(user=user)
    order = OrderItem(user=user)
    

    context={
        'order':order,
    }
    return render(r,'your-order.html',context)

def wish(r):
    return render(r,'wish.html')

def aboutus(r):
    return render(r,'aboutus.html')

from django.shortcuts import render
from .models import product 
from .models import categorie

def systembuilder(request):
    return render(request, 'system.html')

def changedpasswd(r):
    return render(r,'success.html')

def error(r):
    return render(r,'unsuccess.html')

def nouser(r):
    return render(r,'nouser.html')

def home(r):
    p = product.objects.filter(status='PUBLISH')

    context = {
        'product':p
    }
    return render(r,'index.html',context)

def products(request):
    p = product.objects.filter(status='PUBLISH')
    CATEGORIES = categorie.objects.all()
    FILTER=filter_price.objects.all()
    COLOR=color.objects.all()
    BRAND=brand.objects.all()
    review = Review.objects.all() 
   
    CATID= request.GET.get("categories")
    BRANDID=request.GET.get("brand")
    FILTERID=request.GET.get("filter_price")
    COLORID=request.GET.get("color")
    ATOZID =request.GET.get("ATOZ")
    ZTOAID =request.GET.get("ZTOA")
    PRICE_LOWTOHIGHID=request.GET.get("PRICE_LOWTOHIGH")
    PRICE_HIGHTOLOWID=request.GET.get("PRICE_HIGHTOLOW")
    NEW_PRODUCTID=request.GET.get("NEW_PRODUCT")
    OLD_PRODUCTID=request.GET.get('OLD_PRODUCT')


    if CATID:
        p= product.objects.filter(categories= CATID , status='PUBLISH')
    elif BRANDID:
        p= product.objects.filter(brand= BRANDID , status='PUBLISH')
    elif FILTERID:
        p= product.objects.filter(filter_price= FILTERID , status='PUBLISH')
    elif COLORID:
        p= product.objects.filter(color= COLORID , status='PUBLISH')
    elif ATOZID:
        p= product.objects.filter(status='PUBLISH').order_by('name')
    elif ZTOAID:
        p= product.objects.filter(status='PUBLISH').order_by('-name')
    elif PRICE_LOWTOHIGHID:
        p= product.objects.filter(status='PUBLISH').order_by('price')
    elif PRICE_HIGHTOLOWID:
        p= product.objects.filter(status='PUBLISH').order_by('-price')
    elif NEW_PRODUCTID:
        p= product.objects.filter(status='PUBLISH',Condition='new').order_by('-id')
    elif OLD_PRODUCTID:
        p= product.objects.filter(status='PUBLISH',Condition='old').order_by('-id')
    
    else:
        p= product.objects.filter(status='PUBLISH')

    context = {
        'product':p,
        'categorie':CATEGORIES,
        'filter_price':FILTER,
        'color':COLOR,
        'brand':BRAND,
    }
    return render(request,'product.html',context)

def search(r):
    query=r.GET.get('query')
    products=product.objects.filter(name__icontains=query)

    context={
    'product':products
    }
    return render(r,'search.html',context)

def products_detail(r,id):
    prod=product.objects.get(id=id)
    
    context={
        'prod':prod
    }
    return render(r,'single_product.html',context)

def contact_page(r):
    if r.method == 'POST':
        name= r.POST.get('name')
        email=r.POST.get('email')
        subject =r.POST.get('subject')
        message=r.POST.get('message')

        # Save the user's response first
        contact=contactus(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        contact.save()

        # Then try to send the email
        email_from=settings.EMAIL_HOST_USER
        try:
            send_mail(subject, message, email_from,)
        except:
            # If the email fails to send, redirect to 'contact' but the user's response is still saved
            return redirect('contact')

        return redirect('home') 

    return render(r,'contact.html')

from django.http import JsonResponse
def HandleRegister(r):
 if r.method == 'POST':
    userrname = r.POST.get('username')
    fname = r.POST.get('fname')
    lname = r.POST.get('lname')
    email = r.POST.get('email')
    phone = r.POST.get('call')
    pass1 = r.POST.get('pass1')
    pass2 = r.POST.get('pass2')

    if User.objects.filter(username__iexact=userrname).exists():
        messages.warning(r, "A user with this username already exists.")
    elif len(userrname) > 10 or len(userrname) < 3:
        messages.warning(r, "User Name should be between 3 to 10 characters!")
    elif len(pass1) > 10 or len(pass2) > 10:
        messages.warning(r, "Let’s keep your password under 10 characters, alright? 😊")
    elif pass1 != pass2:
        messages.warning(r, "Your Password does not match. 🔐")
    else:
        customer = User.objects.create_user(username=userrname, email=email, password=pass1,)
        customer.first_name = fname
        customer.last_name = lname
        customer.save()
        messages.success(r, 'Congratulations! Your account has been successfully created. 👍👍')
        return redirect('regis.html')
    return redirect('register.html')
 return render(r, 'register.html')



""" 
                        

            """
def HandleLogin(r):
    if r.method =='POST':
        username=r.POST.get('username')
        password=r.POST.get('password')
        

        user = authenticate(username=username,password=password)
        if user is not None:
            login(r,user)
            return redirect('loigis.html')
        elif user is None:
            messages.warning(r,'Please Enter Correct Username and Password!!')
        else:
            return redirect('login')

    return render(r,'login.html')

def HandleLogout(r):
    logout(r)
    return redirect('/')

def forgetpassword(r):
    if r.method == 'POST':
        username = r.POST['username']
        new_password = r.POST['password']
        confirm_password = r.POST['confirm_password']

        if new_password != confirm_password:
            return  redirect('unsuccess.html',)

        User = get_user_model()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return redirect('nouser.html')

        user.set_password(new_password)
        user.save()

        # Redirect to a success page
        return redirect('success.html')

    return render(r,'forgetpass.html')


@login_required(login_url="/login.html")
def cart_add(request, id):
    cart = Cart(request)
    prod = product.objects.get(id=id)
    cart.add(prod)
    return redirect("home")

@login_required(login_url="/login.html")
def wish_add(request, id):
    cart = Cart(request)
    prod = product.objects.get(id=id)
    cart.add(prod)
    return redirect("home")

@login_required(login_url="/login.html")
def wish_clear(request, id):
    cart = Cart(request)
    prod  = product.objects.get(id=id)
    cart.remove(prod)
    return redirect("cart_details")

@login_required(login_url="/login.html")
def item_clear(request, id):
    cart = Cart(request)
    prod  = product.objects.get(id=id)
    cart.remove(prod)
    return redirect("wish")

@login_required(login_url="/login.html")
def wish_increment(request, id):
    cart = Cart(request)
    prod  = product.objects.get(id=id)
    cart.add(prod)
    return redirect("wish")

@login_required(login_url="/login.html")
def item_increment(request, id):
    cart = Cart(request)
    prod  = product.objects.get(id=id)
    cart.add(prod)
    return redirect("cart_details")


@login_required(login_url="/login.html")
def wish_decrement(request, id):
    cart = Cart(request)
    prod = product.objects.get(id=id)
    cart.decrement(prod)
    return redirect("wish")


@login_required(login_url="/login.html")
def item_decrement(request, id):
    cart = Cart(request)
    prod = product.objects.get(id=id)
    cart.decrement(prod)
    return redirect("cart_details")


@login_required(login_url="/login.html")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_details")

@login_required(login_url="/login.html")
def wish_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("wish")


@login_required(login_url="/login.html")
def wish_detail(request):
    return render(request, 'wish.html')

@login_required(login_url="/login.html")
def cart_detail(request):
    return render(request, 'cart/cart_details.html')

@login_required
def all(request):
    current_user = request.user
    orders = OrderItem.objects.filter(user=current_user)

    context = {
        'orders': orders,
        'user': current_user,
    }
    return render(request, 'all.html', context)


def Check_out(r):
    amount_str=r.POST.get('amount')
    print("amount_str")
    print(amount_str)
    amount_float=float(amount_str)
    amount=int(amount_float *100)

    payment =client.order.create(
        {
            "amount": amount,
            "currency": "INR",
            "payment_capture":"1"
        }
    )
    order_id=payment['id']
    context={
        "order_id" :order_id,
        "payment" : payment,
    }
    return render(r,"cart/checkout.html",context)

def Place_order(r):
    if r.method == "POST":
        uid=r.session.get('_auth_user_id')
        user=User.objects.get(id = uid)
        
        cart=r.session.get('cart')
    
    
        

        firstname=r.POST.get('firstname')
        lastname =r.POST.get('lastname')
        country =r.POST.get('country')
        address =r.POST.get('address')
        city=r.POST.get('city')
        state=r.POST.get('state')
        postcode=r.POST.get('postcode')
        phone=r.POST.get('phone')
        email=r.POST.get('email')
        amount=r.POST.get('amount')
    
        
        order_id= r.POST.get('order_id')
        payment =r.POST.get('payment')

        context={
            'order_id':order_id,
       }
        
        order= Order(
            user=user,
            firstname=firstname,
            lastname=lastname,
            country=country,
            address=address,
            city=city,
            state=state,
            postalcode=postcode,
            phone=phone,
            email=email,
            Paymentid=order_id,
            amount=amount,
            Paid=True,


        )  
        order.save()
        for i in cart:
            a=(int(cart[i]['price']))
            b=cart[i]['quantity']
            
            total=a*b

            item =OrderItem(
                user=user,
                order=order,
                products=cart[i]['name'],
                image=cart[i]['image'],
                quantity=cart[i]['quantity'],
                price=cart[i]['price'],
                total=total
            ) 
            item.save()
        
        return render(r,'cart/placeorder.html',context)
    else:
       return render(r,'cart/placeorder.html')
    
@csrf_exempt
def success(r):
    if r.method == "POST":
        a = r.POST
        order_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
        
        user = Order.objects.filter(Paymentid=order_id).first()
        if user is not None:
            user.paid=True
            user.save()
        else:
            print(f"No Order found with Paymentid: {order_id}")
        
    return render(r, 'cart/thank-you.html')

def invoice(r):
    return render(r,'pdf_convert/invoicedetail.html')

