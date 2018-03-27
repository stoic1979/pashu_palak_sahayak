from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import UserProfile,AddAnimal
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ( 'mobile_no', 'state','district','tehsil','village',)


class AddAnimalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddAnimal
        fields = ( 'name', 'animal_type','tag_no','dob','stage',)
    