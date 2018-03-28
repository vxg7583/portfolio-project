from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.allpics, name='allpics'),
    path('<int:pics_id>/', views.det, name="det"),
]
