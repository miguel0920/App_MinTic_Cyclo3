from django.db import models

class ModelBase(models.Model):
    createDateTime = models.DateTimeField()
    updateDateTime = models.DateTimeField(null=True)
    isActive = models.BooleanField()

    class Meta:
        abstract = True