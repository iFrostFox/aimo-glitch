from django.urls import path
from . import views


app_name = 'newsroom'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('newsroom/newspaper/<SLUG>/', views.newspaper_detail, name='newspaper_detail'),
    path('newsroom/', views.newsroom, name='newsroom'),
    path('howtoguide/', views.howtoguide, name='howtoguide'),
]
