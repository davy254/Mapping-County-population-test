from django.urls import path
from .views import county_view,MainPageView




urlpatterns = [
    path('countydata/',county_view,name='county'),
    path('',MainPageView.as_view(),name='main'),

]