from django.db.models import Q
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

    def validate(self, attrs):
        email = attrs['email']
        email_queryset = User.objects.filter(email=email)
        if email_queryset.exists():
            raise ValidationError("This email already registered.")
        return attrs

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
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token'
        ]

    def validate(self, attrs):
        user_obj = None
        email = attrs.get("email", None)
        username = attrs.get("username", None)
        password = attrs["password"]
        if not email and not username:
            raise ValidationError('A username or email is required to login.')

        user = User.objects.filter(Q(email=email) | Q(username=username)).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError('this username/email is not valid.')

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials please try again.")

        attrs["token"] = "SOME RANDOM TOKEN"

        return attrs