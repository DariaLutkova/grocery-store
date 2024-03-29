from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from rest_framework import status

from .models import Product
from .models import LoyaltyCard
from .models import Reviews
from .serializers import ProductSerializer
from .serializers import LoyaltyCardSerializer
from .serializers import ReviewSerializer

class ProductView(APIView):
  def get(self, request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response({'products': serializer.data})

  def post(self, request):
    product = request.data.get("product")

    serializer = ProductSerializer(data = product)
    if serializer.is_valid(raise_exception=True):
      product_saved = serializer.save()

    return Response({"success": "Product '{}' has been added".format(product_saved.name)})

  def delete(self, request, pk):
    product = get_object_or_404(Product.objects.all(), pk=pk)
    product.delete()
    return Response({
      "message": "Product with id '{}' has been deleted".format(pk)
      }, status=204)

  def put(self, request, pk):
    product_saved = get_object_or_404(Product.objects.all(), pk=pk)
    data = request.data.get("product")
    serializer = ProductSerializer(instance=product_saved, data=data, partial=True)

    if serializer.is_valid(raise_exception=True):
      product_saved = serializer.save()

    return Response({
      "success": "Product '{}' has been updated".format(product_saved.name)
    })

class LoyaltyCardView(APIView):
  def get(self, request):
    loyaltyCards = LoyaltyCard.objects.all()
    serializer = LoyaltyCardSerializer(loyaltyCards, many=True)

    return Response({'cards': serializer.data})

class ReviewView(APIView):
    def get(self, request):
        reviews = Reviews.objects.all()
        serializer = ReviewSerializer(reviews, many=True)

        return Response({'reviews': serializer.data})

class AuthView(APIView):
  def post(self, request):
      username =  request.data.get("username")
      password = request.data.get("password")
      loggedUser = authenticate(username=username, password=password)

      if loggedUser is not None:
        if loggedUser.is_active:
          login(request, loggedUser)

          if loggedUser.groups.filter(name='customer').exists():
             return Response({
                "role": "customer",
                "firstName": loggedUser.first_name,
                "lastName": loggedUser.last_name,
                "email": loggedUser.email
              })
          elif loggedUser.groups.filter(name='operator').exists():
             return Response({
                  "firstName": loggedUser.first_name,
                  "lastName": loggedUser.last_name,
                  "email": loggedUser.email,
                  "role": "operator",
                })
          else:
            print(loggedUser.first_name, 'LOGGED USER')
            return Response({
               "role": "administrator",
               "firstName": loggedUser.first_name,
               "lastName": loggedUser.last_name,
               "email": loggedUser.email
             })
        else:
          return Response({
                  "error": "disabled account"
          })
      else:
        return Response({
        "error": "invalid login or password"
        })

class UserView(APIView):
  def get(self, request):
   if request.user.groups.filter(name='customer').exists():
       return Response({
         "isAuth": request.user.is_authenticated,
         "firstName": request.user.first_name,
         "lastName": request.user.last_name,
         "email": request.user.email,
         "role": "customer",
       })
   elif request.user.groups.filter(name='operator').exists():
     return Response({
       "isAuth": request.user.is_authenticated,
       "firstName": request.user.first_name,
       "lastName": request.user.last_name,
       "email": request.user.email,
       "role": "operator",
     })
   else:
      return Response({
          "isAuth": request.user.is_authenticated,
          "firstName": request.user.first_name,
          "lastName": request.user.last_name,
          "email": request.user.email,
          "role": "administrator",
        })

class LogoutView(APIView):
  def post(self, request):
      logout(request)
      return Response({"status":"success"})

class RegistrationView(APIView):
  def post(self, request):
    user = User.objects.create(
      username=request.data.get('username'),
      email=request.data.get('email'),
      first_name=request.data.get('firstName'),
      last_name=request.data.get('lastName')
    )

    user.set_password(str(request.data.get('password')))
    user.save()

    group = Group.objects.get(name='customer')
    group.user_set.add(user)

    return Response({
        "status":"success",
        "response":"User Successfully Created",
        "role": "customer"
    }, status=status.HTTP_201_CREATED)

