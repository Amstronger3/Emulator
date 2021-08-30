from datetime import timezone

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View

from scheduler.models import Profile


def index(request):
    return render(request, 'index.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class ProfileView(View):

    def get(self, request, *args, **kwargs):
        user = Profile.objects.get(user=request.user)
        time = user.last_update_time.replace(tzinfo=timezone.utc).astimezone(tz=None).strftime("%Y/%m/%d %H:%M")
        return render(request, 'profile.html', {'user': user, 'time': time})
