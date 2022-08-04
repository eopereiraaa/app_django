from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_polls2'),
    path('test/', views.test, name='test'),
    path('test_html/', views.test_html, name='test_html'),
    path('casa/test_html_two/', views.test_html_two, name='test_html_two'),
    path('conversor/', views.conversor, name='conversor'),
]