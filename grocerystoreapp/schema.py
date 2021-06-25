import graphene
from graphene_django import DjangoObjectType

from grocerystore.models import Product
from grocerystore.models import ProductType
from grocerystore.models import Supplier
from grocerystore.models import Store
from grocerystore.models import Sale
from grocerystore.models import LoyaltyCard
from grocerystore.models import Reviews

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
class StoresType(DjangoObjectType):
    class Meta:
        model = Store
class SuppliersType(DjangoObjectType):
    class Meta:
        model = Supplier
class SalesType(DjangoObjectType):
    class Meta:
        model = Sale
class LoyaltyCardType(DjangoObjectType):
    class Meta:
        model = LoyaltyCard
class ReviewsType(DjangoObjectType):
    class Meta:
        model = Reviews
class Query(graphene.ObjectType):
    products = graphene.List(ProductType)
    loyaltyCards = graphene.List(LoyaltyCardType)
    reviews = graphene.List(ReviewsType)
    stores = graphene.List(StoresType)
    suppliers = graphene.List(SuppliersType)
    sales = graphene.List(SalesType)

    def resolve_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_loyaltyCards(self, info, **kwargs):
        return LoyaltyCard.objects.all()

    def resolve_reviews(self, info, **kwargs):
        return Reviews.objects.all()

    def resolve_stores(self, info, **kwargs):
            return Store.objects.all()

    def resolve_suppliers(self, info, **kwargs):
                return Supplier.objects.all()

    def resolve_sales(self, info, **kwargs):
                return Sale.objects.all()

class CreateProduct(graphene.Mutation):
    name = graphene.String()
    productType = graphene.Int()
    supplier = graphene.Int()
    store = graphene.Int()
    sale = graphene.Int()
    price = graphene.Float()
    priceSale = graphene.Float()
    count = graphene.Int()
    date = graphene.String()
    isNew =graphene.Boolean()
    image = graphene.String()


    class Arguments:
        name = graphene.String()
        productType = graphene.Int()
        supplier = graphene.Int()
        store = graphene.Int()
        sale = graphene.Int()
        price = graphene.Float()
        priceSale = graphene.Float()
        count = graphene.Int()
        date = graphene.String()
        isNew =graphene.Boolean()
        image = graphene.String()


    def mutate(name, productType, supplier, store, sale, price, priceSale, count, date, isNew, image):
        productType = ProductType.objects.get(id=product_type_id)
        supplier = Supplier.objects.get(id=supplier_id)
        store = Store.objects.get(id=store_id)
        sale = Sale.objects.get(id=sale_id)
        product = Product(
          name=name,
          productType=productType,
          supplier=supplier,
          store=store,
          sale=sale,
          price=price,
          priceSale=priceSale,
          count=count,
          date=date,
          isNew=isNew,
          image=image,
          )
        product.save()

        return CreateProduct(
          name=product.name,
          productType=product.productType,
          supplier=product.supplier,
          store=product.store,
          sale=product.sale,
          price=product.price,
          priceSale=product.priceSale,
          count=product.count,
          date=product.date,
          isNew=product.isNew,
          image=product.image,
        )

class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()

class CreateSale(graphene.Mutation):
    name = graphene.String()
    description = graphene.String()


    class Arguments:
        name = graphene.String()
        description = graphene.String()


    def mutate(name, description):
        sale = Sale(
          name=name,
          description=description
          )
        sale.save()

        return CreateSale(
          name=sale.name,
          description=sale.description
        )

class Mutation(graphene.ObjectType):
    create_sale = CreateSale.Field()

schema = graphene.Schema(
  query=Query,
  mutation=Mutation
)