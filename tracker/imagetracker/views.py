import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from imagetracker.models import ImageHash, ImageVisit


def image(request, hash):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')

    image_hash = get_object_or_404(ImageHash, hash=hash)
    visit = ImageVisit(image=image_hash, ip=ip_address, data=str(request.META))
    visit.save()
    image_data = open(image_hash.location, "rb").read()
    return HttpResponse(image_data, content_type=image_hash.header)
