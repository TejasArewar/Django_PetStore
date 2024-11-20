from django.urls import path
from.import views

urlpatterns = [
    path('', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('profile_pic/<int:id>/', views.profile_pic, name = 'profile_pic'),
    path('delete_profile_pic/<int:id>/', views.delete_profile_pic, name = 'delete_profile_pic'),
]