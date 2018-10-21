from django.db import models
from django.contrib.auth import get_user_model
from image_groups.models import ImageGroup
from django.utils.timezone import now as django_time_now

user_model = get_user_model()

class Photo(models.Model):
    owner = models.ForeignKey(user_model, on_delete=models.CASCADE)
    group = models.ForeignKey(ImageGroup, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=False)
    tag = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    date_posted = models.DateTimeField(editable=False, blank=True, default=django_time_now)
    date_taken = models.DateTimeField(editable=False, blank=True, null=True)
    location = models.FilePathField(path='assets/images/', recursive=True)

    def __str__(self):
        return "Photo: (id={}, title={})".format(self.id, self.title)