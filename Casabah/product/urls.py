from django.urls import path
from . import views

urlpatterns = [path("", views.index, name="home-page"),
               path("product", views.product, name="product-page"),
               path("newproduct/", views.createproduct, name="create-page"),
               path("newingredient/", views.createingredient, name="create-ingredient"),
               path("updateproduct/<str:pk>", views.updateproduct, name="update-page"),

               ]
