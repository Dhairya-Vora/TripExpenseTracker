from django.db import models
from django.utils import timezone

class expense(models.Model):
    name = models.TextField(null=False)
    type = models.TextField()
    remarks = models.TextField()
    amount = models.FloatField()
    time = models.TextField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.time = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        super().save(*args, **kwargs)


