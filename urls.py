import django.urls
from catalog import views

urlpatterns = [

    django.urls.path('', views.index, name='index'),
    django.urls.path('', views.home, name='home'),
    django.urls.path('contact/', views.contact, name='contact'),
    django.urls.path('', views.home, name='home'),
    django.urls.path('contact/', views.contact, name='contact'),

]