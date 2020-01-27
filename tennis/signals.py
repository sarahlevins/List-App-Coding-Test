from django.core.signals import request_finished
from django.dispatch import receiver
from .models import PageViews

@receiver(request_finished)
def pageviewcount(sender, **kwargs):
    count = PageViews(count=0)
    count.save()

