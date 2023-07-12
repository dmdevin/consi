from django.db import models

# Create your models here.
class Scanners(models.Model):
    sn = models.CharField(max_length=250)
    serial = models.CharField(max_length=250)
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "scanners"
