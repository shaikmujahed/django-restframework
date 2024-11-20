from rest_framework import serializers
from restframework_validation.models import Number


class NumberSerializer(serializers.Serializer):
    even_field = serializers.IntegerField()

    def create(self, validated_data):
        return Number.objects.create(**validated_data)


    

