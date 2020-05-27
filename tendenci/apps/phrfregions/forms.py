from tendenci.apps.phrfregions.models import Phrfregion
from tendenci.apps.perms.forms import TendenciBaseForm
from django import forms
from django.utils.translation import ugettext_lazy as _


class PhrfregionForm(TendenciBaseForm):

    status_detail = forms.ChoiceField(
        choices=(('active', _('Active')),
                 ('inactive', _('Inactive')),
                 ('pending', _('Pending')),))

    class Meta:
        model = Phrfregion
        fields = (
        'name',
#        'update_dt',
        'allow_anonymous_view',
        'user_perms',
        'member_perms',
        'group_perms',
        'status',
        'status_detail',
        )

        fieldsets = [(_('Phrfregion Information'), {
                      'fields': ['name',],   # 'update_dt'],
                      }),
                      (_('Permissions'), {
                      'fields': ['allow_anonymous_view',
                                 'user_perms',
                                 'member_perms',
                                 'group_perms',
                                 ],
                      'classes': ['permissions'],
                      }),
                     (_('Administrator Only'), {
                      'fields': ['status',
                                 'status_detail'],
                      'classes': ['admin-only'],
                    })]


#    def __init__(self, *args, **kwargs):
#        super(IndustryForm, self).__init__(*args, **kwargs)
#
#        if not self.user.profile.is_superuser:
#            if 'status' in self.fields:
#                self.fields.pop('status')
#            if 'status_detail' in self.fields:
#                self.fields.pop('status_detail')
