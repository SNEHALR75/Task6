from django.urls import path
from product_app.api import ProductAPI


urlpatterns = [
    path('product/',ProductAPI.as_view()),
]