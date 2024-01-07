from django.urls import path
from . import views
from django.contrib import admin    
from store import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('aboutus/', views.aboutPage, name="aboutus"),
    path('contactus/', views.contactPage, name="contactus"),
    path('',views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('contactus/', views.contactPage),  
]