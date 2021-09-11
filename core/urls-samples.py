from django.urls import path
from . import views

app_name = 'ukazky'
urlpatterns = [
    path('flask_blueprints', views.Sample1View.as_view(), name='flask_blueprints'),
    path('list_comprehension', views.Sample2View.as_view(), name='list_comprehension'),
    path('program_anagram', views.Sample3View.as_view(), name='program_anagram'),
    path('test3', views.Sample4View.as_view(), name='test3'),
    path('test4', views.Sample5View.as_view(), name='test4'),
    path('test5', views.Sample6View.as_view(), name='test5'),
]
