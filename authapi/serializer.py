from rest_framework import serializers
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name','last_name')
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

class CustomJWTSerializer(JSONWebTokenSerializer):
    email_field = 'email'

    def validate(self, attrs):

        password = attrs.get("password")
        user_obj = User.objects.filter(email__iexact=attrs.get("email")).first()
        if user_obj is not None:
            credentials = {
                'email':user_obj.email,
                'password': password
            }
            if all(credentials.values()):
                user = authenticate(**credentials)
                if user:
                    if not user.is_active:
                        msg = _('User account is disabled.')
                        raise serializers.ValidationError(msg)

                    payload = jwt_payload_handler(user)

                    return {
                        'token': jwt_encode_handler(payload),
                        'user': user
                    }
                else:
                    msg = {"error":_('Incorrect password.')}
                    raise serializers.ValidationError(msg)

            else:
                msg = {"error":_('Must include "{email_field}" and "password".')}
                # msg = msg.format(email_field=self.email_field)
                raise serializers.ValidationError(msg)
        else:
            msg = {"error":_('Account with this email/username does not exists')}
            raise serializers.ValidationError(msg)

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

class ResetEmailSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset email
    """
    email = serializers.EmailField()
    def validate(self, attrs):
        email = attrs.get('email')
        user = User.objects.filter(email__iexact=email).first()
        if not user:
            raise serializers.ValidationError('Invalid Email!')
        return attrs

class PasswordTokenSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    token = serializers.CharField()