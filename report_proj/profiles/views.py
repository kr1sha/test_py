from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import ProfileForms


@login_required
def my_profile_views(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForms(request.POST or None, request.FILES or None, instance=profile)
    confirm = False

    if form.is_valid():
        form.save()
        confirm = True

    context = {
        'profile': profile,
        'form': form,
        'confirm': confirm
    }
    return render(request, 'profiles/main.html', context)
