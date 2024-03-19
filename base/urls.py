"""
URL configuration for myproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from . import views


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
        # ...
 
        return token
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


urlpatterns = [
    path('',views.home),
    path('categories/', views.category_list),
    path('categories/<int:pk>/', views.category_detail),
    # Paths for Product model
    path('products/', views.product_list),
    path('products/<int:pk>/', views.product_detail),
    # Paths for Order model
    path('orders/', views.order_list),
    path('orders/<int:pk>/', views.order_detail),
    # Paths for OrderDetail model
    path('orderdetails/', views.orderdetail_list),
    path('orderdetails/<int:pk>/', views.orderdetail_detail),
    path('siginin/', MyTokenObtainPairView.as_view()),
    path('register/', views.register),
]

