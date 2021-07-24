from django.db import models
from django.db.models.deletion import CASCADE
from cpf_field.models import CPFField

class PersonType(models.Model):
    name = models.CharField(max_length=32, null=False, unique=True)
    def __str__(self) -> str:
        return self.name


class PersonMediaType(models.Model):
    name = models.CharField(max_length=32, null=False, unique=True)
    def __str__(self) -> str:
        return self.name


class Person(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=32, null=False)
    type = models.ForeignKey(PersonType, on_delete=CASCADE, null=False)
    cpf = CPFField('cpf', null=False, unique=True)
    phone = models.CharField(max_length=15, null=True)
    company = models.CharField(max_length=32, null=False)
    last_update = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name


class PersonMedia(models.Model):
    person = models.ForeignKey(Person, on_delete=CASCADE, null=True)
    media_type = models.ForeignKey(PersonMediaType, on_delete=CASCADE, null=True)
    object_media = models.ImageField(upload_to='persons', max_length=256)
    def __str__(self) -> str:
        return self.person + ' ' + self.media_type


class PersonAudit(models.Model):
    person = models.ForeignKey(Person, on_delete=CASCADE, null=False)
    type = models.IntegerField(null=False)
    cpf_new = CPFField('cpf_new', null=False)
    cpf_old = CPFField('cpf_old', null=True)
    last_update = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.person + ' ' + self.cpf_new