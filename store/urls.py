from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home_page'), #home page
    path('store', views.store, name='store_page'),
    path('aboutus', views.aboutus, name='aboutus_page'),
    path('thanku', views.thanku, name='thanku_page'),
    path('signup', views.signup, name='signup_page'), #new user
    path('login', views.login, name='login_page'), #already exist user
    # path('logout0', views.logout0, name='logout0_page'),
    path('logout', views.logout, name='logout_page'),
    path('cart', views.cart, name='cart_page'),
    # path('emptyCart', views.emptyCart, name='emptyCart_page'),
    path('checkout0', views.checkout0, name='checkout0_page'), #to go to checkout page
    path('checkout', views.checkout, name='checkout_page'),
    path('orders', views.orders, name='orders_page'),
    path('payment', views.payment, name='payment_page'),
]