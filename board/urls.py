from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='login'),
    path('daily_connect/', views.afterlogin, name='daily_connect'),
    path('<int:board_id>/', views.detail, name='detail'),
    path('create/', views.create.as_view(), name='create'),
]