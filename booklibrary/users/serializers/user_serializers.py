from booklibrary.users.validators import number_validator, special_char_validator, letter_validator
from rest_framework import serializers
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model
User = get_user_model()


class InputRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=70)
    password = serializers.CharField(
            validators=[
                    number_validator,
                    letter_validator,
                    special_char_validator,
                    MinLengthValidator(limit_value=10)
                ]
            )
    confirm_password = serializers.CharField(max_length=255)
    
    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("username Already Taken")
        return username

    def validate(self, data: dict):
        if not data.get("password") or not data.get("confirm_password"):
            raise serializers.ValidationError("Please fill password and confirm password")
        
        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError("confirm password is not equal to password")
        return data

class OutPutRegisterSerializer(serializers.ModelSerializer):
    # token = serializers.SerializerMethodField("get_token")
    class Meta:
        model = User 
        fields = ("username", "created_at", "updated_at")

class UserFilterSerializer(serializers.Serializer):
    is_active = serializers.BooleanField(
        required=False, allow_null=True, default=None
    )
