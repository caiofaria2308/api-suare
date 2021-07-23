from django.contrib import admin
from person.models import Person, PersonAudit
from person.models import PersonMedia, PersonMediaType, PersonType

admin.register(Person)
admin.register(PersonAudit)
admin.register(PersonMediaType)
admin.register(PersonMedia)
admin.register(PersonType)