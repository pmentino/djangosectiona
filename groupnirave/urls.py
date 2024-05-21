from django.urls import path
from .import views

urlpatterns = [
    path('genders', views.index_gender),
    path('genders/create', views.create_gender),
    path('gender_store', views.store_gender),
]
