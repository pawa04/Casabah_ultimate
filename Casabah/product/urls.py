from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path("", views.index, name="home-page"),
               path("login/", views.loginPage, name="login-page"),
               path("logout/", views.logoutPage, name="logout-page"),
               path("product/<str:pk>", views.product, name="product-page"),
               path("newproduct/", views.createproduct, name="create-page"),
               path("newingredient/", views.createingredient, name="create-ingredient"),
               path("updateproduct/<str:pk>", views.updateproduct, name="update-page"),
               path("deleteproduct/<str:pk>", views.deleteproduct, name="delete-page"),
               ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#hello



