from django.shortcuts import render

## Create your views here.

#
#@login_required
#def edit(request, id, form_class=BoatForm, template_name="boats/edit.html"):
#    user_edit = get_object_or_404(User, pk=id)
#
#    try:
#        profile = Profile.objects.get(user=user_edit)
#    except Profile.DoesNotExist:
#        profile = Profile.objects.create_profile(user=user_edit)
#    if profile.language == 'en-us':
#        profile.language = 'en'
#
#    if not profile.allow_edit_by(request.user): raise Http403
#
#    required_fields = get_setting('module', 'users', 'usersrequiredfields')
#    if required_fields:
#        required_fields_list = required_fields.split(',')
#        required_fields_list = [field.strip() for field in required_fields_list]
#    else:
#        required_fields_list = None
#
#    if request.method == "POST":
#        form = form_class(request.POST,
#                          user_current=request.user,
#                          user_this=user_edit,
#                          required_fields_list=required_fields_list,
#                          instance=profile)
#
#        if form.is_valid():
#            # get the old profile, so we know what has been changed in admin notification
#            old_user = User.objects.get(id=id)
#            old_profile = Profile.objects.get(user=old_user)
#            profile = form.save(request, user_edit)
#
#            if request.user.profile.is_superuser:
#                # superusers cannot demote themselves
#                if user_edit == request.user:
#                    security_level = 'superuser'
#                    if form.cleaned_data['security_level'] != 'superuser':
#                        messages.add_message(request, messages.INFO, _("You cannot convert yourself to \"%(role)s\" role.") % {'role' : form.cleaned_data['security_level']})
#                else:
#                    security_level = form.cleaned_data['security_level']
#
#                if security_level == 'superuser':
#                    user_edit.is_superuser = 1
#                    user_edit.is_staff = 1
#                    # remove them from auth_group if any - they don't need it
#                    user_edit.groups = []
#                elif security_level == 'staff':
#                    user_edit.is_superuser = 0
#                    user_edit.is_staff = 1
#                else:
#                    user_edit.is_superuser = 0
#                    user_edit.is_staff = 0
#                    # remove them from auth_group if any
#                    user_edit.groups = []
#
#                # set up user permission
#                profile.allow_user_view, profile.allow_user_edit = False, False
#
#            else:
#                user_edit.is_superuser = 0
#                user_edit.is_staff = 0
#
#            # interactive
#            interactive = form.cleaned_data['interactive']
#            try:
#                interactive = int(interactive)
#            except:
#                interactive = 0
#            if interactive == 1:
#                user_edit.is_active = 1
#            else:
#                user_edit.is_active = 0
#
#            user_edit.save()
#            profile.save()
#
#            # update member-number on profile
#            profile.refresh_member_number()
#
#            # notify ADMIN of update to a user's record
#            if get_setting('module', 'users', 'userseditnotifyadmin'):
#            #    profile_edit_admin_notify(request, old_user, old_profile, profile)
#                # send notification to administrators
#                recipients = get_notice_recipients('module', 'users', 'userrecipients')
#                if recipients:
#                    if notification:
#                        extra_context = {
#                            'old_user': old_user,
#                            'old_profile': old_profile,
#                            'profile': profile,
#                            'request': request,
#                        }
#                        notification.send_emails(recipients,'user_edited', extra_context)
#
#            return HttpResponseRedirect(reverse('profile', args=[user_edit.username]))
#    else:
#        if profile:
#            form = form_class(user_current=request.user,
#                          user_this=user_edit,
#                          required_fields_list=required_fields_list,
#                          instance=profile)
#
#        else:
#            form = form_class(user_current=request.user,
#                          user_this=user_edit,
#                          required_fields_list=required_fields_list)
#
#    return render_to_resp(request=request, template_name=template_name,
#        context={'user_this':user_edit, 'profile':profile, 'form':form,
#                                              'required_fields_list':required_fields_list})
#
#
