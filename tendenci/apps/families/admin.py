from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from tendenci.apps.perms.admin import TendenciBaseModelAdmin
from tendenci.apps.families.models import Family
from tendenci.apps.families.forms import FamilyForm


class FamilyAdmin(TendenciBaseModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'date_of_birth', 'email', 'update_dt']
    list_filter = []
    search_fields = ['user', 'first_name', 'last_name', 'date_of_birth', 'email', 'user__username', 'user__first_name', 'user__last_name', 'user__email']
    fieldsets = (
        ('',               {'fields': ('user', 'first_name', 'last_name', 'date_of_birth', 'email')}),
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
    form = FamilyForm
    ordering = ['-update_dt']

admin.site.register(Family, FamilyAdmin)

# Register your models here.
