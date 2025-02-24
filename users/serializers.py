from rest_framework import serializers
from .models import CustomUser
from django.utils.translation import gettext_lazy as _



class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "password", "full_name", "password2"]

    def validate(self, data):
        password = data['password']
        password2 = data['password2']

        if password != password2:
            raise serializers.ValidationError({'passwords':'Passwords do not match'})
    
        return data
    
    

class ResendOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    

class VerifyOtpSerializer(ResendOtpSerializer):
    otp = serializers.IntegerField()


class ResendOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()

class VerifyOtpSerializer(ResendOtpSerializer):
    otp = serializers.IntegerField()

class SetNewPasswordSerializer(VerifyOtpSerializer):
    password = serializers.CharField(
        min_length=8, error_messages={'min_length': _("{min_length} characters min.")}
    )

class LoginSerializer(ResendOtpSerializer):
    password = serializers.CharField()

class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()


        










