from django.urls import path
from . import views

app_name = 'ukazky'
urlpatterns = [
    path('flask_blueprint', views.Sample1View.as_view(), name='flask_blueprint'),
    path('list_comprehension', views.Sample2View.as_view(), name='list_comprehension'),
    path('python_anagram', views.Sample3View.as_view(), name='python_anagram'),
    path('python_property', views.Sample4View.as_view(), name='python_property'),
    path('python_matrix', views.Sample5View.as_view(), name='python_matrix'),
    path('regular_expression', views.Sample6View.as_view(), name='regular_expression'),
]
