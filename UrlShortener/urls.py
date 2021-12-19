from django.contrib import admin
from django.urls import path
from shortener.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CreateUrlView.as_view(), name='home-page'),
    path('result/<int:pk>/', DetailUrlView.as_view(), name='result'),
]
