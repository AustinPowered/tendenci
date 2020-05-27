from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from tendenci.apps.perms.admin import TendenciBaseModelAdmin
from tendenci.apps.phrfregions.models import Phrfregion
from tendenci.apps.phrfregions.forms import PhrfregionForm


class PhrfregionAdmin(TendenciBaseModelAdmin):
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
    form = PhrfregionForm
    ordering = ['-update_dt']

admin.site.register(Phrfregion, PhrfregionAdmin)

# Register your models here.

# Register your models here.
