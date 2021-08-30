from celery import shared_task
from django.utils import timezone

from .models import Profile


@shared_task
def check_payment():
    user_profiles = Profile.objects.all()
    for profile in user_profiles:
        if profile.payment == 'PAID':
            profile.last_update_time = timezone.now()
        profile.save()
