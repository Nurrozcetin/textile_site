from django.contrib import admin
from .models import Event, Customer

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("model", "error", "date" ,"orderNo","customer_list",)
    search_fields = ("model",)

    def customer_list(self, obj):
        html = ""
        for customer in obj.customers.all():
            html += customer.name + " "
        return html

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "customer_count",)
    prepopulated_fields = {"name": ("name",),}

    def customer_count(self, obj):
        return obj.customer_set.count()
    