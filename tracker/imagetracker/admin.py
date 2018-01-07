from django.contrib import admin

from .models import ImageHash, ImageVisit


class ImageHashAdmin(admin.ModelAdmin):
    list_display = ('hash', 'location', 'header')
    fields = ['hash', 'location', 'header']


class ImageVisitAdmin(admin.ModelAdmin):
    list_display = ('image', 'ip', 'data')
    fields = ['image', 'ip', 'data']


admin.site.register(ImageHash, ImageHashAdmin)
admin.site.register(ImageVisit, ImageVisitAdmin)
