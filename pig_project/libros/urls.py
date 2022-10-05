from django.urls import path
from . import views


urlpatterns=[
    path('',views.vacio),
    path('nada/',views.nada),
    path('saludo/serio/<str:nombre>/',views.saludo_serio),
    path('saludo/<str:nombre>/', views.saludo),
    path('despedida/', views.despedida) ,
    path('index/', views.index)
    #repath(r'')

]
