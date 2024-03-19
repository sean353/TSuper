from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
  """Model for product categories"""
  name = models.CharField(max_length=255)
 

  def __str__(self):
    return self.name

class Product(models.Model):
  """Model for products in the supermarket"""
  name = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Order(models.Model):
  """Model for customer orders"""
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  is_completed = models.BooleanField(default=False)

  def __str__(self):
    return f"Order #{self.id} - {self.user.username}"

class OrderDetail(models.Model):
  """Model for details of each item in an order"""
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField()
  total = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return f"{self.quantity}x {self.product.name} (Order #{self.order.id})"
