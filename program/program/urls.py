from django.contrib import admin
from django.urls import path
from rizalprog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about),
    path('services/', views.services),
    path('blog/', views.blog),
    path('contact/', views.contact),
]
