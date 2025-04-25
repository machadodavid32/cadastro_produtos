from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),  # Página inicial
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),  # Página de cadastro
]
