from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    # le entregamos la ruta de la categoria y el dinamismo a la url
    path('category/<int:category_id>/', views.category, name="category")
]