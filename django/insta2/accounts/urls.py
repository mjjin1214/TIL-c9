from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.lists, name='lists'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_id>/', views.detail, name='detail'),
    path('<int:user_id>/follow', views.follow, name='follow'),
    path('edit/', views.edit, name='edit'),
]