from django.contrib import admin

from .models import Store, Position, Staff, Supplier, ProductType, Product, Check, LoyaltyCard, Sale, Reviews


admin.site.register(Store)
admin.site.register(Position)
admin.site.register(Staff)
admin.site.register(Supplier)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Check)
admin.site.register(LoyaltyCard)
admin.site.register(Sale)
admin.site.register(Reviews)