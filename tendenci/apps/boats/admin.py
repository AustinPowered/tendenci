from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from tendenci.apps.perms.admin import TendenciBaseModelAdmin
from tendenci.apps.boats.models import Boat
from tendenci.apps.boats.forms import BoatForm


class BoatAdmin(TendenciBaseModelAdmin):
    list_display = ['user', 'name', 'sailnumber', 'boatclass', 'rating', 'phrfregion', 'hullcolor', 'make', 'model', 'update_dt']
    list_filter = []
    search_fields = ['user', 'name', 'boatclass', 'phrfregion', 'user__username', 'user__first_name', 'user__last_name', 'user__email']
    fieldsets = (
        ('',               {'fields': ('user', 'name', 'sailnumber', 'boatclass', 'rating', 'phrfregion', 'hullcolor', 'make', 'model')}),
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
    form = BoatForm
    ordering = ['-update_dt']

admin.site.register(Boat, BoatAdmin)

# Register your models here.
