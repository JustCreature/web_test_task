from django.db import models

# Create your models here.

class Site(models.Model):

    name = models.CharField(max_length=200)
    url = models.URLField(null=False, blank=False, default=" 1 ")
    status = models.BooleanField(null=False,
                                 blank=False,
                                 default=False)
    updated_at = models.DateTimeField(null=False,
                                      blank=False,
                                      auto_now_add=True)

    def __str__(self):
        return f"{self.name}"