from django.urls import path
from ams import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',views.login_page,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout_page,name='logout'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('tracker',views.tracker,name='tracker'),
    path('prodview/<int:myid>',views.productView,name='prodview'),
    path('checkout',views.checkout),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)