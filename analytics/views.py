from django.shortcuts import render

# Create your views here.
from .models import Recommendation
from .serializers import RecommendationSerializer
from django.http import HttpResponse
from rest_framework import viewsets, status


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all().order_by('id')
    serializer_class = RecommendationSerializer
    #]permission_classes = [permission.IsAu]