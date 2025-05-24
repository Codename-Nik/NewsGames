from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page

from Newa.views import HomeNewa, NewaByCategory, ViewNewa, AddNewa, register, user_login, user_logout
#from Newa.views import index, get_category, view_newa, add_newa, test

urlpatterns = [
   #path('', index, name='Home'),
   #path('category/<int:category_id>/', get_category, name='Category'),
   #path('newa/<int:news_id>/', view_newa, name='View_newa'),
   #path('newa/add_newa', add_newa, name='Add_newa')
   #path('test/', test, name='Test'),
    path('', HomeNewa.as_view(), name='Home'),
    path('category/<int:category_id>/', NewaByCategory.as_view(), name='Category'),
    path('newa/<int:pk>/', ViewNewa.as_view(), name='View_newa'),
    path('newa/add_newa', AddNewa.as_view(), name='Add_newa'),
    path('register/', register, name='Register'),
    path('login/', user_login, name='Login'),
    path('logout/', user_logout, name='Logout'),
]
