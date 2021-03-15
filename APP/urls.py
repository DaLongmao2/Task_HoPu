from django.urls import path

from APP import views


urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('detailed/<id>', views.detailed, name='detailed'),
]
