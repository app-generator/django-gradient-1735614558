# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    role = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Patient(models.Model):

    #__Patient_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    sex = models.CharField(max_length=255, null=True, blank=True)
    birthdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    address = models.CharField(max_length=255, null=True, blank=True)
    contact_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    #__Patient_FIELDS__END

    class Meta:
        verbose_name        = _("Patient")
        verbose_name_plural = _("Patient")


class Admission(models.Model):

    #__Admission_FIELDS__
    is_readmission = models.BooleanField()
    diagnosis = models.TextField(max_length=255, null=True, blank=True)
    treatment = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    remarks = models.TextField(max_length=255, null=True, blank=True)
    clinician = models.CharField(max_length=255, null=True, blank=True)
    patient = models.CharField(max_length=255, null=True, blank=True)

    #__Admission_FIELDS__END

    class Meta:
        verbose_name        = _("Admission")
        verbose_name_plural = _("Admission")



#__MODELS__END
