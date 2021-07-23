from person.models import Person, PersonMediaType, PersonMedia, PersonType, PersonAudit
from .serializers import PersonAuditSerializer, PersonMediaSerializer, PersonMediaTypeSerializer, PersonMediaTypeSerializer, PersonSerializer, PersonTypeSerializer
from rest_framework import viewsets


class PersonTypeViewSet(viewsets.ModelViewSet):
    queryset = PersonType.objects.all()
    serializer_class = PersonTypeSerializer


class PersonMediaTypeViewSet(viewsets.ModelViewSet):
    queryset = PersonMediaType.objects.all()
    serializer_class = PersonMediaTypeSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonMediaViewSet(viewsets.ModelViewSet):
    queryset = PersonMedia.objects.all()
    serializer_class = PersonMediaSerializer


class PersonAuditViewSet(viewsets.ModelViewSet):
    queryset = PersonAudit.objects.all()
    serializer_class = PersonAuditSerializer