from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('profile/', views.profile, name = 'profile'),
    path('pet/', views.pet, name = 'pet'),
    path('cart/', views.cart, name = 'cart'),
    path('savetocart/<int:id>/', views.savetocart, name = 'savetocart'),
    path('remove_cart/<int:id>/', views.remove_cart, name = 'remove_cart'),
    path('orders/', views.orders, name = 'orders'),
    path('wishlist/', views.wishlist, name = 'wishlist'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('pay/', views.pay, name = 'pay'),
    path('logout/', views.logout, name = 'logout'),
    path('search/', views.search, name = 'search'),
    path('update_quantity/<int:id>/<str:action>/', views.update_quantity, name = 'update_quantity'),
    path('buyapet/<int:id>/', views.buyapet, name = 'buyapet'),
    path('buyallpets/', views.buyallpets, name = 'buyallpets'),

    path('payment/<int:amount>/',views.payment,name="payment"),    
    path('success/<int:amount>/<int:id>/<str:payment_id>/<str:address>/<int:session>/',views.success,name="success"),
]