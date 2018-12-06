from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import authenticate
from django.conf import  settings
from django.contrib.auth.models import User
from django.template import loader

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework_jwt.settings import api_settings
from rest_framework import status
import jwt
from artmain.settings import SECRET_KEY

from django.core.mail import EmailMultiAlternatives


from .serializer import UserSerializer, ResetEmailSerializer, PasswordTokenSerializer, LoginSerializer
from .models import ResetPasswordToken

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# Create your views here.

class LoginView(APIView):
    """
    Login using username or email and password
    return JWT token if logged in successfully
    """
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        # validation
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username_or_email = serializer.validated_data['username_or_email']
        password = serializer.validated_data['password']

        # check the existance of user
        user_obj = User.objects.filter(email__iexact=username_or_email).first() or User.objects.filter(
            username__iexact=username_or_email).first()
        if user_obj:
            credentials = {
                'username': user_obj.username,
                'password': password
            }
            if all(credentials.values()):
                user = authenticate(**credentials)

                if user:
                    if not user.is_active:
                        msg=_('User account is disabled.')
                        return Response({
                            'message':msg,
                            'status':'failed'
                        }, status=status.HTTP_400_BAD_REQUEST)

                    # return JWT token
                    payload = jwt_payload_handler(user)
                    msg = {
                        'token':jwt.encode(payload, SECRET_KEY),
                        'status':'success',
                        'user'  : user.username
                    }
                    return Response(msg, status=status.HTTP_200_OK)
                else:
                    return Response(
                        {
                            'error':'invalid Credential',
                            'status': 'failed'
                        },status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                msg = {
                    'message' : 'Must include "{username_field}" and "password".',
                    'status': 'failed',
                }
                return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        else:
            msg = {
                'message':'Account with this email/username does not exists',
                'status' :'failed'
            }
            return Response(msg, status=status.HTTP_404_NOT_FOUND)


class RegisterView(APIView):
    """
    Register View
    """
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        # validation
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

            username = request.data['username']
            email = request.data['email']
            password = request.data['password']
            first_name = request.data['first_name']
            last_name = request.data['last_name']

            # check email in user
            user = User.objects.filter(email__iexact=email).first()
            if user:
                msg = {
                    'status'  : 'failed',
                    'message' : 'Email is already existed.'
                }
                return Response(msg, status=status.HTTP_400_BAD_REQUEST)
            # check username in user
            user = User.objects.filter(username__iexact=username).first()
            if user:
                msg={
                    'status': 'failed',
                    'message': 'Username is already existed.'
                }
                return Response(msg, status=status.HTTP_400_BAD_REQUEST)

            # create new User
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.set_password(password)
            user.is_active = True
            user.save()
            msg = {
                'status':'success',
                'user' : username
            }
            return Response(msg, status=status.HTTP_201_CREATED)

        else:
            msg = {
                'status' : 'failed',
                'message': 'Invalid parameters'
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)


def get_password_reset_token_expiry_time():
    """
    Returns the password reset token expirty time in hours (default: 24)
    Set Django SETTINGS.DJANGO_REST_MULTITOKENAUTH_RESET_TOKEN_EXPIRY_TIME to overwrite this time
    :return: expiry time
    """
    # get token validation time
    return getattr(settings, 'DJANGO_REST_MULTITOKENAUTH_RESET_TOKEN_EXPIRY_TIME', 24)


class ResetPasswordRequestToken(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        # validation of request
        serializer = ResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']

        # before we continue, delete all existing expired tokens
        password_reset_token_validation_time = get_password_reset_token_expiry_time()

        # datetime.now minus expiry hours
        now_minus_expiry_time = timezone.now() - timedelta(hours=password_reset_token_validation_time)

        # delete all expired reset tokens
        ResetPasswordToken.objects.filter(created_at__lte=now_minus_expiry_time).delete()

        #find a user with email
        user = User.objects.filter(email__iexact=email).first()

        if not user:
            return Response(
                {
                    "status": "failed",
                    "message": "There is not user associated with this email address"
                }, status=status.HTTP_404_NOT_FOUND
            )
        # if user is not active or unusable password
        elif not ( user.is_active and user.has_usable_password()):
            return Response(
                {
                    "status": "failed",
                    "message": "There is no active user associated with this e-mail address or the password can not be changed"
                }, status=status.HTTP_404_NOT_FOUND
            )
        else:
            token = None
            if user.password_reset_tokens.all().count()>0:
                token = user.password_reset_tokens.all()[0]
            else:
                token = ResetPasswordToken.objects.create(
                    user=user,
                    user_agent=request.META['HTTP_USER_AGENT'],
                    ip_address=request.META['REMOTE_ADDR']
                )
            self.send_mail(token=token)
            return Response(
                {   "status" : "success",
                    "message": "Message was sent to {}".format(token.user.email)
                }, status=status.HTTP_200_OK
            )
    def send_mail(self, token):
        subject, from_email, to = 'hello', 'no-reply@gmail.com', token.user.email
        text_content = 'This is an important message.'
        link = "http://127.0.0.1:8000/resetpassword/?token=" + token.key
        html_content = loader.render_to_string('reset_template.html',{'link':link})

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True

class ResetPasswordConfirm(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = PasswordTokenSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        old_password = serializer.validated_data['old_password']
        new_password = serializer.validated_data['new_password']
        token = serializer.validated_data['token']

        # get token validation time
        get_password_reset_token_validation_time = get_password_reset_token_expiry_time()

        # search token
        reset_password_token = ResetPasswordToken.objects.filter(key=token).first()

        if reset_password_token is None:
            return Response({
                "status":"success",
                "message":"Token not found"
            }, status=status.HTTP_404_NOT_FOUND)

        # check expiry date
        expiry_date = reset_password_token.created_at + timedelta(hours=get_password_reset_token_validation_time)

        if timezone.now() > expiry_date:
            # delete expired token
            reset_password_token.delete()
            return Response({
                "status":"failed",
                "message":"Token was expired"
            }, status=status.HTTP_404_NOT_FOUND)
        if not old_password == reset_password_token.user.password:
            return Response({
                "status":"failed",
                "message":"Incorrect old password"
            }, status=status.HTTP_404_NOT_FOUND)
        if reset_password_token.user.has_usable_password():
            reset_password_token.user.set_password(new_password)
            reset_password_token.user.save()
        # delete used token
        ResetPasswordToken.filter(user=reset_password_token.user).delete()
        return Response({
            "status":"success",
            "message":"successfully changed"
        })

@api_view(['GET'])
def test(request):
    return Response("test",status=status.HTTP_200_OK)
