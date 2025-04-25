from django.urls import path
from . import views


urlpatterns = [
 path('personagens/', views.personagens_lista, name='personagens_lista'),
 ]