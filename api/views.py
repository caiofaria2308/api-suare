from person.models import Person, PersonMediaType, PersonMedia, PersonType, PersonAudit
from django.contrib.auth.models import User
from .serializers import PersonAuditSerializer, PersonMediaSerializer, PersonMediaTypeSerializer
from .serializers import PersonMediaTypeSerializer, PersonSerializer
from .serializers import PersonTypeSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class PersonTypeViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PersonType.objects.all()
    serializer_class = PersonTypeSerializer


class PersonMediaTypeViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PersonMediaType.objects.all()
    serializer_class = PersonMediaTypeSerializer


class PersonViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonMediaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PersonMedia.objects.all()
    serializer_class = PersonMediaSerializer


class PersonAuditViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PersonAudit.objects.all()
    serializer_class = PersonAuditSerializer


class LoggedUserViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer