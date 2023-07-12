from rest_framework import serializers
from .models import Scanners

class ScannersSerializer(serializers.ModelSerializer):
    sn = serializers.CharField(max_length=250)
    serial = serializers.CharField(max_length=250)
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Scanners
        fields = '__all__'