from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
   
   path('signup/', SignUpView.as_view(), name='signup'),
   path('api/users/', CustomUserListCreate.as_view(), name='user-list'),
   path('api/users/<int:pk>/', CustomerUserRetriveUpdateDestory.as_view(), name='user-detail'),
]