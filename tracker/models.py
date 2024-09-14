from django.db import models

# Create your models here.
class EmailTracking(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=255)
    opened = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email