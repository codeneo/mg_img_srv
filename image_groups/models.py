from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now as django_time_now

user_model = get_user_model()

class ImageGroup(models.Model):
    owner = models.ForeignKey(user_model, related_name='owner', on_delete=models.PROTECT)
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(editable=False, blank=True, default=django_time_now)
    users = models.ManyToManyField(user_model, related_name='users', blank=True)

    def __str__(self):
        return "ImageGroup: (id={}, title={})".format(self.id, self.name)