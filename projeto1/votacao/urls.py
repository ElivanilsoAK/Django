from django.urls import path

from . import views

app_name = 'votacao'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_questao>/', views.detalhe, name='detalhe'),
    path('<int:id_questao>/votar/', views.votar, name='votar'),
    path('<int:id_questao>/resultado/', views.resultado, name='resultado'),
]  