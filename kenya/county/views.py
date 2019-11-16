from django.shortcuts import render
import json
from django.http import JsonResponse , HttpResponse
from django.core.serializers import serialize
from .models import County
from django.views.generic import  TemplateView
from django.core.cache import cache
# Create your views here.
"""def county_view(request):
    county_geojson = serialize('geojson',County.objects.all())
    return JsonResponse(json.loads(county_geojson))
"""


def county_view(request):
    counties = serialize('geojson', County.objects.all())
    #return HttpResponse(counties, content_type='application/json')
    return JsonResponse(json.loads(counties))


class MainPageView(TemplateView):
    template_name = 'county/main.html'

class Map1PageView(TemplateView):
    template_name = 'county/map1.html'
