from django.urls import path
from .views import county_view,MainPageView,Map1PageView



app_name = 'county'
urlpatterns = [
    path('countydata/',county_view,name='county'),
    path('',MainPageView.as_view(),name='main'),
    path('map1/',Map1PageView.as_view(),name='map1'),

]