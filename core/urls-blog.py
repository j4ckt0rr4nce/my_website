from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('co_je_datova_analyza/', views.blog_1, name='co_je_datova_analyza'),
    path('co_je_kniznica_numpy/', views.blog_2, name='co_je_kniznica_numpy'),
    path('co_je_kniznica_pandas/', views.blog_3, name='co_je_kniznica_pandas'),
]
