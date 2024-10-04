from django.urls import path
from . import views 

urlpatterns = [
    path('generate-titles/', views.generate_titles_view, name='generate_titles')
]
