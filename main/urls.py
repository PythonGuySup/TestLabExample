from django.urls import path
from TestLabExample.main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/<str:pg>', views.home_page, name='home_page')
]
