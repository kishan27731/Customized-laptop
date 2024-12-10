from tkinter import Place
from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
 #path('admin/',admin.site.urls),
    path("",views.home,name="home"),
    path('base/',views.base,name="base"),
    path('product/',views.products,name="product"),
    path('search/',views.search,name="search"),
    path('product/<str:id>',views.products_detail,name="single_product"),
    path('contact/',views.contact_page,name="contact"),
    path('register.html',views.HandleRegister,name="register"),
    path('login.html',views.HandleLogin,name="login"),
    path('logout/',views.HandleLogout,name="logout"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('messages/',views.message,name="messages"),
    path('prof/',views.profil,name="prof"),
    path('prof/pro.html',views.pr,name="pro"),
    path('pro.html',views.pr,name="pro"),
    path('regis.html',views.pr,name="pro"),
    path('loigis.html',views.pr,name="pro"),
    path('req/',views.re,name="request"),
    path('forget/',views.forgetpassword,name="forget"),
    path('system/',views.systembuilder,name="system"),
    path('success/',views.changedpasswd,name="successfull"),
    path('unsuccess/',views.error,name="unsuccessfull"),
    path('nouser/',views.nouser,name="nouser"),
    path('allorders/',views.all,name="allorders"),
    path('wish.html',views.wish, name='wish'),
    path('track/',views.track , name='track'),
    path('Cancel/',views.Cancel , name='cancel'),
    path('done/',views.done , name='done'),
    path('review/',views.save_review, name='save_review'),
    path('compare/',views.compare, name='compare'),


    

#add to cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
     path('wish/add/<int:id>/', views.wish_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('wish/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.wish_increment, name='item_increment'),
     path('wish/item_increment/<int:id>/',views.wish_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('wish/item_decrement/<int:id>/',views.item_decrement, name='wish_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart_details/',views.cart_detail,name='cart_details'),
    path('system/<int:id>/', views.systembuilder, name='systembuilder'),
   path('cart/cart_details/product/',views.products,name='cart/cart_details/products'),

#add review 
  path('product/<int:product_id>/review/', views.save_review, name='submit_review'),   

#add review cmpleted 

    path('cart/checkout/',views.Check_out,name="checkout"),
    path('cart/placeorder/',views.Place_order,name="place_order"),
    path('forget/success.html',views.changedpasswd,name="success"),
    path('forget/unsuccess.html',views.error,name="unsuccessfull"),
    path('forget/nouser.html',views.nouser,name="nouser"),
    path('success',views.success,name="success"),
    path('your-order',views.your_order,name="your_order"),
    path('allorder',views.all,name="allorder"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)