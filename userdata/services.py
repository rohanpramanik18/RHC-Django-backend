import dataclasses
import datetime
import jwt
from typing import TYPE_CHECKING
from django.conf import settings
from . import models
from django.shortcuts import get_object_or_404
from rest_framework import exceptions

if TYPE_CHECKING:
    from .models import User, Asha, Patient

@dataclasses.dataclass
class UserDataClass:
    first_name: str
    last_name: str
    email: str
    password: str = None
    id: int = None

    @classmethod
    def from_instance(cls, user: "User") -> "UserDataClass":
        return cls(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            id=user.id,
        )
        

@dataclasses.dataclass
class AshaDataClass:
    first_name: str
    last_name: str
    email: str
    phone_number : str
    password: str = None
    id: int = None

    @classmethod
    def from_instance(cls, asha: "Asha") -> "AshaDataClass":
        return cls(
            first_name=asha.first_name,
            last_name=asha.last_name,
            email=asha.email,
            id=asha.asha_id,
            password = asha.password,
            phone_number=asha.phone_number
        )        
        
        
        
@dataclasses.dataclass
class PatientDataClass:
    created_by : models.Patient.created_by
    first_name: str
    last_name: str
    gender : str
    id_proof : str
    patient_pic : str
    phone_number : str
    # id_proof : __file__
    id: int = None
    

    @classmethod
    def from_instance(cls, patient: "Patient") -> "PatientDataClass":
        return cls(
            first_name=patient.first_name,
            last_name=patient.last_name,
            gender = patient.gender,
            id=patient.patient_id,
            id_proof = patient.id_proof,
            patient_pic = patient.patient_pic,
            phone_number=patient.phone_number,
            created_by = patient.created_by
        )        




##  USER SERVICES
def create_user(user_dc: "UserDataClass") -> "UserDataClass":
    instance = models.User(
        first_name=user_dc.first_name, 
        last_name=user_dc.last_name, 
        email=user_dc.email
    )
    if user_dc.password is not None:
        instance.set_password(user_dc.password)

    instance.save()

    return UserDataClass.from_instance(instance)


def user_email_selector(email: str) -> "User":
    user = models.User.objects.filter(email=email).first()

    return user


def create_token(user_id: int) -> str:
    payload = dict(
        id=user_id,
        exp=datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        iat=datetime.datetime.utcnow(),
    )
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")

    return token



def modify_user (user_id: int, user_dc: "UserDataClass"):
    user = get_object_or_404(models.User, pk=user_id)
    models.User.objects.filter(pk=user_id).update(
        first_name=user_dc['first_name'], 
        last_name=user_dc['last_name'], 
        email=user_dc['email'],
        password=user_dc['password']
    )
    # instance.save()
    

    return UserDataClass.from_instance(user)

def delete_user(user: "User", user_id: int) -> "UserDataClass":
    user = get_object_or_404(models.User, pk=user_id)
    user.delete()
    
    
    
    
    
    
    
## ASHA USER SERVICES CRUD
    
    
def create_ashauser(asha_dc: "AshaDataClass") -> "AshaDataClass":
    instance = models.Asha(
        first_name=asha_dc['first_name'], 
        last_name=asha_dc['last_name'], 
        email=asha_dc['email'],
        phone_number=asha_dc['phone_number'],
        password=asha_dc['password'],
    )

    instance.save()

    return AshaDataClass.from_instance(instance)


def ashauser_email_selector(email: str) -> "Asha":
    ashauser = models.Asha.objects.filter(email=email).first()

    return ashauser


def create_ashatoken(asha_id: int) -> str:
    payload = dict(
        id=asha_id,
        exp=datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        iat=datetime.datetime.utcnow(),
    )
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")

    return token



def modify_ashauser (asha_id: int, asha_dc: "AshaDataClass"):
    ashauser = get_object_or_404(models.Asha, pk=asha_id)
    models.Asha.objects.filter(pk=asha_id).update(
        first_name=asha_dc['first_name'], 
        last_name=asha_dc['last_name'], 
        email=asha_dc['email'],
        password=asha_dc['password'],
        phone_number=asha_dc['phone_number']
    )
    # instance.save()
    

    return AshaDataClass.from_instance(ashauser)

def delete_ashauser(ashauser: "Asha", asha_id: int) -> "AshaDataClass":
    ashauser = get_object_or_404(models.Asha, pk=asha_id)
    ashauser.delete()
    
    
    
#PATIENT SERVICES CRUD
    
def create_patient(patient_dc: "PatientDataClass") -> "PatientDataClass":
    print(patient_dc)
    asha_id = models.Asha.objects.filter(pk=patient_dc['created_by']).first()
    instance = models.Patient(
        first_name=patient_dc['first_name'], 
        last_name=patient_dc['last_name'], 
        gender = patient_dc['gender'],
        phone_number=patient_dc['phone_number'],
        id_proof=patient_dc['id_proof'],
        patient_pic=patient_dc['patient_pic'],
        created_by = asha_id
    )

    instance.save()

    # return PatientDataClass.from_instance(instance)


# def patient_email_selector(email: str) -> "Patient":
#     patient = models.Patients.objects.filter(email=email).first()

#     return patient


def create_patienttoken(patient_id: int) -> str:
    payload = dict(
        id=patient_id,
        exp=datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        iat=datetime.datetime.utcnow(),
    )
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")

    return token



def modify_patient (patient_id: int, patient_dc: "PatientDataClass"):
    patient = get_object_or_404(models.Patient, pk=patient_id)
    models.Patient.objects.filter(pk=patient_id).update(
        first_name=patient_dc['first_name'], 
        last_name=patient_dc['last_name'], 
        phone_number=patient_dc['phone_number'],
        patient_pic=patient_dc['patient_pic']
    )
    # instance.save()
    

    return PatientDataClass.from_instance(patient)

def delete_patient(patient: "Patient", patient_id: int) -> "PatientDataClass":
    patient = get_object_or_404(models.Patient, pk=patient_id)
    patient.delete()