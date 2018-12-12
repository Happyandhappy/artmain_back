from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from authapi.permission import TenantAdminPermission
from .serializer import *
# Create your views here.

class UserGroupView(APIView):
    permission_classes = (TenantAdminPermission)

    def get(self, request):
        if request['userType'] is None:
            groups = UserGroup.objects.all()
            msg = {
                'status' : 'success',
                'groups' : groups,
            }
            return Response(msg, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserGroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True):

