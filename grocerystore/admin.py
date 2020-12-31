from django.contrib import admin

from .models import Store, Position, Staff, Supplier, ProductType, Product, Check, LoyaltyCard, Sale, Reviews

class StoreAdmin(admin.ModelAdmin):
	list_display = ('id', 'address', 'city', 'phone_number')
	list_display_links = ('id', 'address', 'city', 'phone_number')
class PositionAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description', 'isFull')
	list_display_links = ('id', 'name', 'description', 'isFull')

class StaffAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'position', 'store', 'salary')
	list_display_links =  ('id', 'name', 'position', 'store', 'salary')
	search_fields = ['name', 'position', 'store']

class SupplierAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'address', 'productType', 'price', 'city')
	list_display_links = ('id', 'name', 'address', 'productType', 'price', 'city')
	search_fields = ['name', 'address', 'productType', 'city']

class ProductTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description')
	list_display_links = ('id', 'name', 'description')

class ProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'productType', 'supplier', 'store', 'sale', 'price', 'priceSale', 'count', 'date', 'isNew', 'image')
	list_display_links = ('id', 'name', 'productType', 'supplier', 'store', 'sale', 'price', 'priceSale', 'count', 'date', 'isNew', 'image')

class CheckAdmin(admin.ModelAdmin):
	list_display = ('id', 'store', 'date', 'total_price', 'loyalty_card')
	list_display_links = ('id', 'store', 'date', 'total_price', 'loyalty_card')

class LoyaltyCardAdmin(admin.ModelAdmin):
	list_display = ('id', 'phone_number', 'scores', 'average_check')
	list_display_links = ('id', 'phone_number', 'scores', 'average_check')

class SaleAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description')
	list_display_links = ('id', 'name', 'description')
class ReviewsAdmin(admin.ModelAdmin):
	list_display = ('id', 'product', 'name', 'text')
	list_display_links = ('id', 'product', 'name', 'text')


admin.site.register(Store, StoreAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Check, CheckAdmin)
admin.site.register(LoyaltyCard, LoyaltyCardAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Reviews, ReviewsAdmin)