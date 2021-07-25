from person.models import Person, PersonMediaType, PersonMedia, PersonType, PersonAudit
from django.contrib.auth.models import User
from rest_framework import serializers


class PersonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonType
        fields = [
            'id',
            'name'
        ]


class PersonMediaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonMediaType
        fields = [
            'id',
            'name'
        ]



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'id',
            'name',
            'type',
            'cpf',
            'phone',
            'company',
            'last_update'
        ]


class PersonMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonMedia
        fields = [
            'id',
            'person',
            'media_type',
            'object_media'
        ]


class PersonAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonAudit
        fields = [
            'id',
            'person',
            'type',
            'cpf_new',
            'cpf_old',
            'last_update'
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name'
        ]