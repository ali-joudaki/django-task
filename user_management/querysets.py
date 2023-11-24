from django.db.models import QuerySet, Sum, Count


class CustomerQuerySet(QuerySet):
    def annotate_with_total_spending(self):
        return self.annotate(total_spending=Sum('order__total_amount'))

    def annotate_with_order_count(self):
        return self.annotate(order_count=Count('order'))