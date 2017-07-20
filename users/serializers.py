from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.Serializer):
	user_id = serializers.CharField(max_length=1000)
	nome = serializers.CharField(max_length=1000)
	token = serializers.CharField(max_length=1000)


	def create(self, validated_data):
		return User.objects.create(**validated_data)


