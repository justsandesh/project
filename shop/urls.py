from django.urls import path
from .views import index, create_order,contact_view,about_view

urlpatterns = [
    path('', index, name='index'),
    path('order/<int:product_id>/', create_order, name='create_order'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about')
]
