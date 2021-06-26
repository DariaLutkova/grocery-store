from rest_framework import serializers
from .models import Product
from .models import LoyaltyCard
from .models import Reviews

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'

class LoyaltyCardSerializer(serializers.ModelSerializer):
	class Meta:
		model = LoyaltyCard
		fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reviews
		fields = '__all__'
