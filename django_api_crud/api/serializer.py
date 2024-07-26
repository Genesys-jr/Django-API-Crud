from rest_framework import serializers
from .models import User


# returns the data in json format
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'