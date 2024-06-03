from django.shortcuts import render
from .models import Listen
import pprint

# Create your views here.
from django.http import HttpResponse


def index(request):
    ls = Listen.objects.filter(lastfm_when__isnull=True, played='Today')
    return HttpResponse(pprint.pprint(ls))
