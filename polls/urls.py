from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),

    path('test_html', views.test_html, name='test_html')
]
