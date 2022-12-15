from django.contrib import admin
# Register your models here.
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email")

admin.site.register(models.User, UserAdmin)

class AshaAdmin(admin.ModelAdmin):
    list_display = ("asha_id", "first_name", "last_name", "email")
    
admin.site.register(models.Asha, AshaAdmin)

class PatientAdmin(admin.ModelAdmin):
    list_display = ("patient_id","patient_pic", "first_name", "last_name","gender", "id_proof")
    
admin.site.register(models.Patient, PatientAdmin)