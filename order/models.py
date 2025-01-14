from django.db import models
from django.db.models import Sum, F, ExpressionWrapper, FloatField
from order.enums import OrderStatus
from order.querysets import OrderQuerySet


class Order(models.Model):
    customer = models.ForeignKey('user_management.Customer', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default=OrderStatus.PENDING, choices=OrderStatus.choices)
    total_price = models.FloatField(default=0)

    objects = OrderQuerySet.as_manager()

    def calculate_total_price(self):
        order_items = self.orderitem_set.all()

        total_price = order_items.aggregate(
            total_price=Sum(ExpressionWrapper(F('product__price') * F('quantity'), output_field=FloatField()))
        )['total_price']

        self.total_price = total_price
        self.save()  # Save the updated total_price to the order
        return total_price or 0
    def accept(self):
        self.status = OrderStatus.ACCEPTED
        self.save()

    def reject(self):
        self.status = OrderStatus.REJECTED
        self.save()

    def deliver(self):
        self.status = OrderStatus.DELIVERED
        self.save()

    def cancel(self):
        self.status = OrderStatus.CANCELLED
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.order.customer.user.username} - {self.product.name}'

    def save(self, *args, **kwargs):
        """You can not modify this method"""
        self.order.total_price = self.order.calculate_total_price()
        self.order.save()
        super().save(*args, **kwargs)
