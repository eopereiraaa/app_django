from django.urls import path
from . import views

# Temos que respeitar esse nome `urlpatterns`
urlpatterns = [
    path('', views.primeira_view, name='first_view')
    # Signature: path(<path: str>, <view: Funcao>, <name: str>)
]
