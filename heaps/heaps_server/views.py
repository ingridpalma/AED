from django.shortcuts import render
from django.utils import timezone
from .models import Device


def post_list(request):
    devices = Device.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'heaps_server/device_list.html', {'devices': devices})

