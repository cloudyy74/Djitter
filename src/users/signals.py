from typing import Any

from django.contrib.auth.models import User
from django.db.models import Model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender: type[Model], instance: User, created: bool, **kwargs: Any):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender: type[Model], instance: User, **kwargs: Any):
    instance.profile.save()
