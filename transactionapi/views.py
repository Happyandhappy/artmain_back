import uuid
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from django.http import HttpResponse, Http404
import csv
from .models import *
from .serializers import *
from .form import UploadFileForm
# Create your views here.



class SnippetView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        snippets = self.get_object(pk=pk)
        serializer = self.serializer(snippets)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        snippets = self.get_object(pk=pk)
        serializer = self.serializer(snippets, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Successfully updated", status=status.HTTP_200_OK)

    def delete(self, request, pk):
        snippet = self.get_object(pk=pk)
        snippet.delete()
        return Response("Successfully deleted", status=status.HTTP_200_OK)

class SnippetListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        tenant = get_tenant(request)
        snippets = self.model.objects.filter(tenant=tenant)
        serializer = self.serializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.create(serializer.validated_data, request)
        return Response("Successfully created", status=status.HTTP_200_OK)

    def create(self, data,request):
        snippet = self.model(**data)
        snippet.tenant = get_tenant(request)
        snippet.save()

"""  F0000Z1 """
class F0000Z1View(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = F0000Z1
    serializer = F0000Z1Serializer

class F0000Z1ListView(SnippetListView):
    permission_classes = (permissions.AllowAny,)
    model = F0000Z1
    serializer = F0000Z1Serializer

""" F00050 """
class F00050View(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = F00050
    serializer = F00050Serializer


class F00050ListView(SnippetListView):
    permission_classes = (permissions.AllowAny,)
    model = F00050
    serializer = F00050Serializer

""" F00051 """
class F00051View(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = F00051
    serializer = F00051Serializer


class F00051ListView(SnippetListView):
    permission_classes = (permissions.AllowAny,)
    model = F00051
    serializer = F00051Serializer

""" F000502 """
class F000502View(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = F000502
    serializer = F000502Serializer


class F000502ListView(SnippetListView):
    permission_classes = (permissions.AllowAny,)
    model = F000502
    serializer = F000502Serializer

""" F00060 """
class F00060View(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = F00060
    serializer = F00060Serializer


class F00060ListView(SnippetListView):
    permission_classes = (permissions.AllowAny,)
    model = F00060
    serializer = F00060Serializer

""" F00061 """
class F00061View(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = F00061
    serializer = F00061Serializer


class F00061ListView(SnippetListView):
    permission_classes = (permissions.AllowAny,)
    model = F00061
    serializer = F00061Serializer

""" F00062 """
class F00062View(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = F00062
    serializer = F00062Serializer


class F00062ListView(SnippetListView):
    permission_classes = (permissions.AllowAny,)
    model = F00062
    serializer = F00062Serializer

""" F00063 """
class F00063View(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = F00063
    serializer = F00063Serializer


class F00063ListView(SnippetListView):
    permission_classes = (permissions.AllowAny,)
    model = F00063
    serializer = F00063Serializer

""" F00064 """
class F00064View(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = F00064
    serializer = F00064Serializer


class F00064ListView(SnippetListView):
    permission_classes = (permissions.AllowAny,)
    model = F00064
    serializer = F00064Serializer

""" F00065 """
class F00065View(SnippetView):
    permission_classes = (permissions.AllowAny,)
    model = F00065
    serializer = F00065Serializer


class F00065ListView(SnippetListView):
    permission_classes = (permissions.AllowAny,)
    model = F00065
    serializer = F00065Serializer


class UploadCSV(APIView):
    permission_classes = (permissions.AllowAny,)

    def handle_uploaded_file(self,f):
        filename = './upload/%s.csv'%(str(uuid.uuid4()))
        with open(filename, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return filename

    def read_csv(self, title, filename, request):
        if title == 'F0000Z1':
            model = F0000Z1
        elif title=='F00050':
            model = F00050
        elif title=='F00051':
            model = F00051
        elif title=='F000502':
            model = F000502
        elif title=='F00060':
            model = F00060
        elif title=='F00061':
            model = F00061
        elif title=='F00062':
            model = F00062
        elif title=='F00063':
            model = F00063
        elif title=='F00064':
            model = F00064
        elif title=='F00065':
            model = F00065
        field_map = model._db_field_map
        fields = []
        tenant = get_tenant(request=request)
        for key in field_map:
            fields.append(key)
        with open(filename,'r') as file:
            csvReader = csv.reader(file)
            header = True
            for row in csvReader:
                if header:
                    header = False
                    continue
                data = {}
                for i in range(len(row)):
                    data[fields[i]] = row[i]
                data['tenant'] = tenant
                snippet = model(**data)
                snippet.save()

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filename = self.handle_uploaded_file(request.FILES['file'])
            self.read_csv(request.POST['title'],filename, request)
            return Response("OK", status=status.HTTP_200_OK)
