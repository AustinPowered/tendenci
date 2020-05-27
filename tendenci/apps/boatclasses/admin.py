from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from tendenci.apps.perms.admin import TendenciBaseModelAdmin
from tendenci.apps.boatclasses.models import Boatclass
from tendenci.apps.boatclasses.forms import BoatclassForm


class BoatclassAdmin(TendenciBaseModelAdmin):
    list_display = ['name', 'update_dt']
    list_filter = []
    search_fields = ['name']
    fieldsets = (
        ('',               {'fields': ('name',)}),
        (_('Permissions'), {'fields': ('allow_anonymous_view',)}),
        (_('Advanced Permissions'), {'classes': ('collapse',), 'fields': (
            'user_perms',
            'member_perms',
            'group_perms',
            )}),
        (_('Status'), {'fields': (
            'status',
            'status_detail',
            )}),
        )
    form = BoatclassForm
    ordering = ['-update_dt']

admin.site.register(Boatclass, BoatclassAdmin)

# Register your models here.
