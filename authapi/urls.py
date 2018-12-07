from django.urls import path, include
from .views import LoginView, RegisterView, ResetPasswordRequestToken,ResetPasswordConfirm, test

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(),name='register'),
    path('resetpassword/', ResetPasswordRequestToken.as_view(), name="resetPassword"),
    path('resetconfirm/', ResetPasswordConfirm.as_view(), name="resetConfirm"),
    path('test/', test, name="test")
]
