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

class UserGroupView(APIView):
    """
    Admin can Only access to this point
    """
    permission_classes = (TenantAdminPermission,)

    def get_object(self, pk):
        try:
            return UserGroup.objects.get(pk=pk)
        except:
            return None


    def get(self, request, pk):
        snippet = self.get_object(pk=pk)
        if not snippet:
            return failedResponse("UserGroup doesnt exist")
        serializer = UserGroupSerializer(snippet)
        return successResponse(serializer.data)

    def post(self, request, pk):
        snippet = self.get_object(pk=pk)
        if not snippet:
            return failedResponse("UserGroup doesnt exist")
        serializer = UserGroupSerializer(snippet, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return successResponse('Successfully updated')

    def delete(self, request, pk):
        snippet = self.get_object(pk=pk)
        if not snippet:
            return failedResponse("UserGroup doesnt exist")
        snippet.delete()
        return successResponse('Successfully deleted')

class UserGroupListView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (TenantAdminPermission,)
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

class PlanView(APIView):
    # permission_classes = (TenantAdminPermission)
    permission_classes = (permissions.AllowAny,)

    def get_object(self, pk):
        try:
            return Plan.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        plan = self.get_object(pk=pk)
        serializer = PlanSerializer(plan)
        return Response(serializer.data)

    def post(self, request, pk):
        plan = self.get_object(pk=pk)
        serializer = PlanSerializer(plan, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return successResponse("Successfully updated!")

    def delete(self, request, pk):
        plan = Plan.objects.get(pk=pk)
        plan.delete()
        return successResponse("Successfully deleted")

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

class ProgramObjectView(APIView):
    permission_classes = (permissions.OR(permissions.IsAdminUser,permissions.IsAuthenticatedOrReadOnly,))

    def get_object(self,pk):
        try:
            return ProgramObject.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = ProgramObjectSerializer(snippet)
        return successResponse(serializer.data)

    def post(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = ProgramObjectSerializer(snippet, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return successResponse("Successfully updated")
    def delete(self,request, pk):
        snippet = self.get_object(pk=pk)
        snippet.delete()
        return successResponse("Successfully deleted")

class ProgramObjectListView(APIView):
    permission_classes = (permissions.AllowAny,)

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

class APIMasterView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = APIMasterSerializer
    def get_object(self, pk):
        try:
            return APIMaster.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = APIMasterSerializer(snippet)
        return successResponse(serializer.data)

    def post(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = APIMasterSerializer(snippet,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return successResponse("Succesfully updated")

class APIMasterListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self,request):
        snippets = APIMaster.objects.all()
        serializer = APIMasterSerializer(snippets, many=True)
        return successResponse(serializer.data)

    def post(self, request):
        serializer = APIMasterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        snippet = APIMaster(**serializer.validated_data)
        snippet.save()
        return successResponse("Successfully created")


class UserView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = UserSerializer(snippet)
        return successResponse(serializer.data)

    def post(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = UserSerializer(snippet, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return successResponse("Succesfully updated")

    def delete(self, request, pk):
        snippet = self.get_object(pk=pk)
        snippet.delete()
        return successResponse("Successfully deleted")

class UserListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        return successResponse(serializer.data)

    def post(self, request):
        serializer = UserSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        snippet  = User.objects.filter(userid__iexact=serializer.validated_data['userid']).first()
        if snippet:
            return failedResponse("User id is already existed")
        snippet = User(**serializer.validated_data)
        snippet.save()
        return successResponse("Successfully created")

class FieldConfigureView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, request, pk):
        try:
            return FieldConfigure.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = FieldConfigureSerializer(snippet)
        return successResponse(serializer.data)

    def post(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = FieldConfigureSerializer(snippet, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return successResponse("Successfull updated")

    def delete(self, request, pk):
        snippet = self.get_object(pk=pk)
        snippet.delete()
        return successResponse("Successfully deleted")

class FieldConfigureListView(APIView):
    permission_classes = (permissions.AllowAny)

    def get(self, request):
        serializer = FieldConfigureSerializer(FieldConfigure.objects.all(), many=True)
        return successResponse(serializer.data)

    def post(self, request):
        serializer = FieldConfigureSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        snippet = FieldConfigure(**serializer.validated_data)
        snippet.save()
        return successResponse("Successfully created")


class FieldUIConfigureView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, pk):
        try:
            return FieldUIConfigure.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = FieldUIConfigureSerializer(snippet)
        return successResponse(serializer.data)

    def post(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = FieldUIConfigureSerializer(snippet, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return successResponse("Successfully updated")

    def delete(self,request, pk):
        snippet = self.get_object(pk=pk)
        snippet.delete()
        return successResponse("Successfully deleted")

class FieldUIConfigureListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        snippets = FieldUIConfigure.objects.all()
        serializer = FieldUIConfigureSerializer(snippets)
        return successResponse(serializer.data)

    def post(self, request):
        serializer = FieldUIConfigureSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        snippet = FieldUIConfigure(**serializer.validated_data)
        snippet.save()
        return successResponse("Successfully created")


class FieldValDefView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, pk):
        try:
            return FieldValDef.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = FieldValDefSerializer(snippet)
        return successResponse(serializer.data)

    def post(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = FieldValDefSerializer(snippet, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return successResponse("Successfully updated")

    def delete(self,request, pk):
        snippet = self.get_object(pk=pk)
        snippet.delete()
        return successResponse("Successfully deleted")

class FieldValDefListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        snippets = FieldValDef.objects.all()
        serializer = FieldValDefSerializer(snippets)
        return successResponse(serializer.data)

    def post(self, request):
        serializer = FieldValDefSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        snippet = FieldValDef(**serializer.validated_data)
        snippet.save()
        return successResponse("Successfully created")


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


class SnippetViewListView(APIView):
    permission_classes = (permissions.AllowAny,)
    model = models.Model
    serializer = serializers.Serializer

    def get(self, request):
        snippets = self.model.objects.all()
        serializer = CustomerSerializer(snippets)
        return successResponse(serializer.data)

    def post(self, request):
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        snippet = self.model(**serializer.validated_data)
        snippet.save()
        return successResponse("Successfully created")
""""""

"""Check primary key from here"""
class ConfigView(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = Config
    serializer = ConfigSerializer


class ConfigListView(APIView):
    permission_classes = (permissions.AllowAny,)
    model = Config
    serializer = ConfigSerializer

class HconfigView(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = Hconfig
    serializer = HconfigSerializer

class HconfigListView(APIView):
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
        serializer = CustomerSerializer(Customer.objects.alll(), many=True)
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
