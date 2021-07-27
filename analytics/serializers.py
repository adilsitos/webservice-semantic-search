from .models import *
from rest_framework import serializers

class RecommendationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Recommendation
        read_only_fields = ['id']
        fields = '__all__'
        