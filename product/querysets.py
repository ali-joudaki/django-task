from django.db.models import QuerySet
from order.models import OrderItem
from django.http import HttpResponse


class ProductQuerySet(QuerySet):
    stock_list = []

    def needs_restock(self):
        """Returns a queryset of products that have a stock less than 10."""
        return self.filter(stock__lt=10)

    def in_stock(self):
        """Returns a queryset of products that are in stock (stock greater than 0)."""
        return self.filter()