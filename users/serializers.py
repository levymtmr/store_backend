from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserCreateSerializer(serializers.ModelSerializer):
    confirm_email = serializers.EmailField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'confirm_email',
            'password'

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        email = data['email']
        email_queryset = User.objects.filter(email=email)
        if email_queryset.exists():
            raise ValidationError("This email already registered.")
        return data

    def validate_email(self, value):
        data = self.get_initial()
        email = data.get('email')
        confirm_email = data.get("confirm_email")
        if email != confirm_email:
            raise ValidationError("Emails must match.")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user_obj = User(
            username=username,
            email=email,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token'
        ]