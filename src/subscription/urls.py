from django.contrib import admin
from django.urls import path
from subscription.views import contact, login_view, logout_view, register_view, update_view, delete_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('update/', update_view, name='update'),
    path('delete/', delete_view, name='delete'),
    path('contact/', contact, name='contact'),
]
