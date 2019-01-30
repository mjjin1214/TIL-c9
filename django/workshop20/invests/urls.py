from django.contrib import admin
from django.urls import path
from . import views

app_name = 'invests'

urlpatterns = [
    path('<int:question_id>/', views.detail, name='detail' ),
    path('', views.index, name='index' ),
    path('<int:question_id>/result', views.result, name='result'),
]
