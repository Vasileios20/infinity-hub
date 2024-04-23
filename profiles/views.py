from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.
# DMcC 09/02/24 Add @login_required decorator to ensure user logged in
@login_required
def profile_detail(request, profile_id):
    """ A view to return a specific profile id """
    if ((request.user.is_authenticated
        and (profile_id == request.user.userprofile.id))
            or (request.user.is_superuser)):

        current_profile = get_object_or_404(UserProfile, id=profile_id)
        # removed the message below as it appears only when the button is
        # pressed, and is confusing to the user
        # messages.info(request, (f'Editing user profile
        # for {current_profile.user}'))

        if request.method == 'POST':
            # user_form = CustomSignupForm(request.POST, request.FILES or None,
            # instance=current_user)
            profile_form = UserProfileForm(request.POST, request.FILES or None,
                                           instance=current_profile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Profile updated successfully')
                return redirect(reverse('profile_detail',
                                        args=[current_profile.id]))
            else:
                messages.error(request, 'Update failed. Please ensure '
                               + 'the form is valid.')
        else:
            profile_form = UserProfileForm(instance=current_profile)

        template = 'profiles/profile.html'
        context = {
            'form': profile_form,
            'on_profile_page': True,
        }

        return render(request, template, context)
    else:
        messages.error(request, 'Restricted: Must have SysAdmin rights to edit'
                       + ' other users profile!')
        return redirect(reverse('home'))


