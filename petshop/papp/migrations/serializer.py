from rest_framework import serializers
from .models import pet_usereg,pet_details


class RegisterSerializer(serializers.ModelSerializer):
    f_name = serializers.CharField(max_length=200)
    l_name = serializers.CharField(max_length=200)
    uname = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    dob = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    gender = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=30)
    ph_no = serializers.IntegerField()

    class Meta:
        model=pet_usereg
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=pet_usereg
        fields='__all__'