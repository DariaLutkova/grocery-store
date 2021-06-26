from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import AuthView
from .views import RegistrationView
from .views import ProductView
from .views import LoyaltyCardView
from .views import ReviewView
from .views import UserView
from .views import LogoutView

app_name = 'product'

urlpatterns = [
	path('products/', ProductView.as_view()),
	path('products/<int:pk>', ProductView.as_view()),
	path('loyaltyCards/', LoyaltyCardView.as_view()),
	path('reviews/', ReviewView.as_view()),
    path('auth/', csrf_exempt(AuthView.as_view())),
    path('registration/', csrf_exempt(RegistrationView.as_view())),
    path('user/', csrf_exempt(UserView.as_view())),
    path('logout/', csrf_exempt(LogoutView.as_view()))
]