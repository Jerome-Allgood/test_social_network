import requests

from django.conf import settings
from rest_framework import serializers, status

from register.models import User
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'email', 'password', 'first_name', 'last_name',)
		write_only_fields = ('password',)
		read_only_fields = ('id',)

	def validate_email(self, value):
		ver_url = f'https://api.hunter.io/v2/email-verifier?email={value}&api_key={settings.EMAILHUNTER_API_KEY}'
		verification = requests.get(ver_url)
		if verification.status_code == status.HTTP_400_BAD_REQUEST or verification.json()['data']['status'] in ['invalid', 'unknown']:
			raise serializers.ValidationError('Email did not pass validation. Please check')

	def create(self, validated_data):
		user = User.objects.create(
			email=validated_data['email'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name']
		)
		user.set_password(validated_data['password'])
		user.save()
		return user