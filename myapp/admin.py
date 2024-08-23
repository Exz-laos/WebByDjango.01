from django.contrib import admin

# from .models import Tracking, Officer
from .models import *
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Author)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("body",)
    list_display = ["id", "title", "images"]
    list_editable = ["title"]


admin.site.register(Post, PostAdmin)


admin.site.register(Tracking)
admin.site.register(Officer)
admin.site.register(AskQA)


class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ("detail",)
    list_display = ["id", "name", "available"]
    list_editable = ["name"]


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "products"]


admin.site.register(Order, OrderAdmin)


class TrackingOrderIDAdmin(admin.ModelAdmin):
    list_display = ["id", "tracking_order"]


admin.site.register(TrackingOrderID, TrackingOrderIDAdmin)

admin.site.register(Category)

admin.site.register(Profile)
admin.site.register(Discount)


# สร้าง Class OrderProductAdmin
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ["id", "product_name"]


admin.site.register(OrderProduct, OrderProductAdmin)


# สร้าง Class CartAdmin
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "product_name"]


admin.site.register(Cart, CartAdmin)


# สร้าง Class CartOrderAdmin
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ["user", "first_name", "last_name"]


admin.site.register(CartOrder, CartOrderAdmin)
