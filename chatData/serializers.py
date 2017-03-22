from rest_framework import serializers
from chatData.models import People

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('username', 'password')
