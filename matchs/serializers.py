from rest_framework import serializers
from matchs.models import Match

class MatchSerializer(serializers.Serializer):
    user_one = serializers.CharField(max_length=1000)
    user_two = serializers.CharField(max_length=1000)
    status = serializers.BooleanField(default=False)

    def create(self, validated_data):
    	return Match.objects.create(**validated_data)
