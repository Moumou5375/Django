from django.urls import path
from . import views

urlpatterns= [
    path('Home', views.Home),
    path('Bar', views.Bar),
    path('donut', views.donut),
    path('graph1', views.graph1),
    path('graph2', views.graph2)
]