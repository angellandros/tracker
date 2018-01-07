from django.db import models


class ImageHash(models.Model):
    hash = models.CharField(max_length=200, db_index=True, unique=True, null=False)
    location = models.CharField(max_length=200)
    header = models.CharField(max_length=50)


class ImageVisit(models.Model):
    image = models.ForeignKey(ImageHash, on_delete=models.CASCADE)
    data = models.CharField(max_length=1000)
    ip = models.CharField(max_length=50)
