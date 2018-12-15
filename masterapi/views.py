from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from django.http import HttpResponse, Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from authapi.permission import TenantAdminPermission
from .serializer import *
from .models import *
# Create your views here.

def successResponse(message):
    msg = {
        'status' : 'success',
        'message' : message
    }
    return Response(msg, status=status.HTTP_200_OK)

def failedResponse(message):
    msg = {
        'status': 'failed',
        'message': message
    }
    return Response(msg, status=status.HTTP_400_BAD_REQUEST)

"""
    Snippet View
"""
class SnippetView(APIView):
    permission_classes = (permissions.AllowAny,)
    model = models.Model
    serializer = serializers.Serializer

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = self.serializer(snippet)
        return successResponse(serializer.data)

    def post(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = self.serializer(snippet, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return successResponse("Successfully updated")

    def delete(self, request, pk):
        snippet = self.get_object(pk=pk)
        snippet.delete()
        return successResponse("Successfully deleted")

"""
    SnippetListView
"""

class SnippetListView(APIView):
    permission_classes = (permissions.AllowAny,)
    model = models.Model
    serializer = serializers.Serializer

    def get(self, request):
        snippets = self.model.objects.all()
        serializer = self.serializer(snippets, many=True)
        return successResponse(serializer.data)

    def post(self, request):
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        snippet = self.model(**serializer.validated_data)
        snippet.save()
        return successResponse("Successfully created")


class UserGroupView(SnippetView):
    """
    Admin can Only access to this point
    """
    permission_classes = (permissions.AllowAny,)
    model = UserGroup
    serializer_class = UserGroupSerializer


class UserGroupListView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserGroupSerializer

    def get_queryset(self):
        return UserGroup.objects.all()

    def get(self, request):
        snippets = self.get_queryset()
        serializer = UserGroupSerializer(snippets, many=True)
        return successResponse(serializer.data)

    def post(self, request):
        serializer = UserGroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        snippet = UserGroup.objects.filter(userType__iexact=serializer.validated_data['userType']).first()
        if snippet:
            return failedResponse("User Type is already existed")
        snippet = UserGroup(**serializer.validated_data)
        snippet.save()
        return successResponse("Successfully created")

class PlanView(SnippetView):
    # permission_classes = (TenantAdminPermission)
    permission_classes = (permissions.AllowAny,)
    model = Plan
    serializer = PlanSerializer

class PlanListView(APIView):
    # permission_classes = (TenantAdminPermission)
    permission_classes = (permissions.AllowAny,)
    serializer_class = PlanSerializer

    def get(self, request):
        serializer = PlanSerializer(Plan.objects.all(), many=True)
        return successResponse(serializer.data)

    def post(self, request):
        serializer = PlanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        plan = Plan.objects.filter(plancode__iexact=serializer.validated_data['plancode']).first()
        if plan:
            return failedResponse("The name of Plan is already exist.")
        plan = Plan(**serializer.validated_data)
        plan.save()
        return successResponse("Successfully created")

class ProgramObjectView(SnippetView):
    # permission_classes = (permissions.OR(permissions.IsAdminUser,permissions.IsAuthenticatedOrReadOnly,))
    model = ProgramObject
    serializer = ProgramObjectSerializer

class ProgramObjectListView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer = ProgramObjectSerializer
    def get(self, request):
        serializer = ProgramObjectSerializer(ProgramObject.objects.all(), many=True)
        return successResponse(serializer.data)

    def post(self, request):
        serializer = ProgramObjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        snippet = ProgramObject.objects.filter(progname__iexact=serializer.validated_data['progname']).first()
        if snippet:
            return failedResponse("Program Object with same name is already existed")
        snippet = ProgramObject(**serializer.validated_data)
        snippet.save()
        return successResponse("Successfully created")

class APIMasterView(SnippetView):
    permission_classes = (permissions.AllowAny,)
    serializer = APIMasterSerializer
    model = APIMaster


class APIMasterListView(SnippetListView):
    permission_classes = (permissions.AllowAny,)
    model = APIMaster
    serializer = APIMasterSerializer


class UserView(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = User
    serializer = UserSerializer

class UserListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        return successResponse(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        snippet  = User.objects.filter(userid__iexact=serializer.validated_data['userid']).first()
        if snippet:
            return failedResponse("User id is already existed")
        snippet = User(**serializer.validated_data)
        snippet.save()
        return successResponse("Successfully created")

class FieldConfigureView(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = FieldConfigure
    serializer = FieldConfigureSerializer


class FieldConfigureListView(SnippetListView):
    permission_classes = (permissions.AllowAny,)
    model = FieldConfigure
    serializer = FieldConfigureSerializer


class FieldUIConfigureView(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = FieldUIConfigure
    serializer = FieldUIConfigureSerializer

class FieldUIConfigureListView(SnippetListView):
    permission_classes = (permissions.AllowAny,)
    model = FieldUIConfigure
    serializer = FieldUIConfigureSerializer


class FieldValDefView(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = FieldValDef
    serializer = FieldValDefSerializer


class FieldValDefListView(SnippetListView):
    permission_classes = (permissions.AllowAny,)
    model = FieldValDef
    serializer = FieldValDefSerializer



"""Check primary key from here"""
class ConfigView(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = Config
    serializer = ConfigSerializer


class ConfigListView(SnippetListView):
    permission_classes = (permissions.AllowAny,)
    model = Config
    serializer = ConfigSerializer

class HconfigView(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = Hconfig
    serializer = HconfigSerializer

class HconfigListView(SnippetListView):
    permission_classes = (permissions.AllowAny,)
    model = Hconfig
    serializer = HconfigSerializer


class CustomerView(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = Customer
    serializer = CustomerSerializer

class CustomerListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        serializer = CustomerSerializer(Customer.objects.all(), many=True)
        return successResponse(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        snippet = Customer.objects.filter(name__iexact=serializer.validated_data['name']).first()
        if snippet:
            return failedResponse("Name is already existed")
        snippet = Customer(**serializer.validated_data)
        snippet.save()
        return successResponse("Successfully created")


class PartnerView(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = Partner
    serializer = PartnerSerializer

class PartnerListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        serializer = PartnerSerializer(Partner.objects.all(), many=True)
        return successResponse(serializer.data)

    def post(self, request):
        serializer = PartnerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        snippet = Partner.objects.filter(name__iexact=serializer.validated_data['name']).first()
        if snippet:
            return failedResponse("Name is already existed")
        snippet = Partner(**serializer.validated_data)
        snippet.save()
        return successResponse("Successfully Created")

class VendorView(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = Vendor
    serializer = VendorSerializer

class VendorListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        serializer = PartnerSerializer(Vendor.objects.all(), many=True)
        return successResponse(serializer.data)

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        snippet = Vendor.objects.filter(name__iexact=serializer.validated_data['name']).first()
        if snippet:
            return failedResponse("Name is already existed")
        snippet = Vendor(**serializer.validated_data)
        snippet.save()
        return successResponse("Successfully Created")

class EmployeeView(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = Employee
    serializer = EmployeeSerializer

class EmployeeListView(APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        serializer = EmployeeSerializer(Employee.objects.all(),many=True)
        return successResponse(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        snippet = Employee.objects.filter(name__iexact=serializer.validated_data['name']).first()
        if snippet:
            return failedResponse("Name is already existed")
        snippet.save()
        return successResponse("Successfully Created")
