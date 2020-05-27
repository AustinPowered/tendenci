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
from tendenci.apps.boats.managers import BoatManager
from tendenci.apps.boatclasses.models import Boatclass
from tendenci.apps.phrfregions.models import Phrfregion


class Boat(TendenciBaseModel):
    id = models.AutoField(primary_key=True)
    # precedence = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=40, unique=True, blank=True)
    sailnumber = models.CharField(max_length=20, blank=True)
    hullcolor = models.CharField(max_length=20, blank=True)
    make = models.CharField(max_length=40, blank=True)
    model = models.CharField(max_length=20, blank=True)
    rating = models.IntegerField(default=0, blank=False)
    user = models.ForeignKey(User, related_name="boats", on_delete=models.CASCADE)              # editable=False
    boatclass = models.ForeignKey(Boatclass, default=0, blank=False, on_delete=models.CASCADE)  # related_name ?? See https://docs.djangoproject.com/en/2.1/topics/db/queries/#backwards-related-objects
    phrfregion = models.ForeignKey(Phrfregion, default= 0, on_delete=models.CASCADE)            # related_name ?? See https://docs.djangoproject.com/en/2.1/topics/db/queries/#backwards-related-objects

#    update_dt = models.DateTimeField(_('Update Date/Time'), null=True, blank=True)     
#    field does not appear in apps/educdations/models.py
#    yet does appear in apps/educdations/admin.py and apps/educdations/settings.json, automatically generated?

    perms = GenericRelation(ObjectPermission,
                                  object_id_field="object_id",
                                  content_type_field="content_type")

    objects = BoatManager()

    class Meta:
        permissions = (("view_boat", _("Can view boat")),)
        verbose_name = _("Boat")
        verbose_name_plural = _("Boats")

    def __str__(self):
        return '%s' %  self.name

    def save(self, *args, **kwargs):
        # self.guid = self.guid or str(uuid.uuid4())

        super(Boat, self).save(*args, **kwargs)
