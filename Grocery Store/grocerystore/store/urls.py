from django.urls import path
from store import views

urlpatterns = [
    path('',views.home),
    path('about',views.about),
    path('contact',views.contact,name='contact'),
    path('add',views.add),
    path('checkout',views.checkout,name='checkout'),
    path('category/<str:name>/',views.category),
    path('stock',views.stock),
]