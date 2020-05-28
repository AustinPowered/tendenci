from builtins import str

import uuid
import ast

from datetime import datetime

from django.db import models
#from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User

from tendenci.apps.perms.models import TendenciBaseModel
from tendenci.apps.perms.object_perms import ObjectPermission
from tendenci.apps.families.managers import FamilyManager


class Family(TendenciBaseModel):
    id = models.AutoField(primary_key=True)
    # precedence = models.PositiveSmallIntegerField()
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(blank=True)
    email = models.EmailField(max_length=254, blank=True)
    user = models.ForeignKey(User, related_name="families", on_delete=models.CASCADE)           # editable=False

#    update_dt = models.DateTimeField(_('Update Date/Time'), null=True, blank=True)     
#    field does not appear in apps/educdations/models.py
#    yet does appear in apps/educdations/admin.py and apps/educdations/settings.json, automatically generated?

    perms = GenericRelation(ObjectPermission,
                                  object_id_field="object_id",
                                  content_type_field="content_type")

    objects = FamilyManager()

    class Meta:
#        permissions = (("view_family", _("Can view family")),)
        verbose_name = _("Family")
        verbose_name_plural = _("Families")

    def __str__(self):
        return '%s' %  " ".join((self.first_name, self.last_name))

    def save(self, *args, **kwargs):
        super(Family, self).save(*args, **kwargs)
