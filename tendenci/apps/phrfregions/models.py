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
from tendenci.apps.phrfregions.managers import PhrfregionManager


class Phrfregion(TendenciBaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, unique=True, blank=False)
#    update_dt = models.DateTimeField(_('Update Date/Time'), null=True, blank=True)     
#    field does not appear in apps/educdations/models.py
#    yet does appear in apps/educdations/admin.py and apps/educdations/settings.json, automatically generated?

    perms = GenericRelation(ObjectPermission,
                                  object_id_field="object_id",
                                  content_type_field="content_type")

    objects = PhrfregionManager()

    class Meta:
    #   permissions = (("view_phrfregion", _("Can view phrfregion")),)
        verbose_name = _("PHRF region")
        verbose_name_plural = _("PHRF regions")

    def __str__(self):
        return '%s' %  self.name
