from django.db import models

class Store(models.Model):
	address = models.CharField(max_length=150)
	city = models.CharField(max_length=100)
	phone_number = models.IntegerField()

	def __str__(self):
		return self.address

class Position(models.Model):
	name = models.CharField(max_length=150)
	description = models.TextField()
	isFull = models.BooleanField()

	def __str__(self):
		return self.name

class Staff(models.Model):
	name = models.CharField(max_length=255)
	birthdate = models.DateField()
	registration_date = models.DateField(auto_now_add=True)
	salary = models.FloatField()
	position = models.ForeignKey('Position', related_name='workers', on_delete=models.CASCADE)
	email = models.EmailField()
	store = models.ForeignKey('Store', related_name='workers', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Supplier(models.Model):
	name = models.CharField(max_length=150)
	address = models.CharField(max_length=150)
	city = models.CharField(max_length=100)
	productType = models.ForeignKey('ProductType', related_name='suppliers', on_delete=models.CASCADE)
	price = models.FloatField()

	def __str__(self):
		return self.name

class ProductType(models.Model):
	name = models.CharField(max_length=150)
	description = models.TextField()

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=150, default = 'default name')
	productType = models.ForeignKey('ProductType', related_name='products', on_delete=models.CASCADE)
	supplier = models.ForeignKey('Supplier', related_name='products', on_delete=models.CASCADE)
	store = models.ForeignKey('Store', related_name='products', on_delete=models.CASCADE)
	sale = models.ForeignKey('Sale', related_name='products', on_delete=models.CASCADE, blank=True,)
	price = models.FloatField()
	priceSale = models.FloatField(blank=True,)
	count = models.FloatField()
	date = models.DateField(auto_now_add=True)
	isNew = models.BooleanField()
	image = models.CharField(max_length=150)

	def __str__(self):
		return self.name


class Check(models.Model):
	store = models.ForeignKey('Store', related_name='checks', on_delete=models.CASCADE)
	products = models.JSONField()
	date = models.DateField(auto_now_add=True)
	total_price = models.FloatField()
	loyalty_card = models.ForeignKey('LoyaltyCard', related_name='checks', on_delete=models.CASCADE, blank=True)
	cashier = models.ForeignKey('Staff', related_name='checks', on_delete=models.CASCADE, default = 0)

	def __str__(self):
		return str(self.id)

class LoyaltyCard(models.Model):
	email = models.CharField(max_length=150, default = 'default name')
	code = models.CharField(max_length=150, default = '000000000')
	scores = models.IntegerField()
	average_check = models.FloatField()

	def __str__(self):
		return str(self.email)

class Sale(models.Model):
	name = models.CharField(max_length=150)
	description = models.TextField()

	def __str__(self):
		return self.name

class Reviews(models.Model):
	name = models.CharField(max_length=150)
	text = models.TextField()
	product = models.ForeignKey('Product', related_name='products', on_delete=models.CASCADE)

	def __str__(self):
		return self.name



