from django.db import models

class ModelBase(models.Model):
    createdatetime = models.DateTimeField()
    updatedatetime = models.DateTimeField(null=True)
    #isactive = models.CharField(max_length=1)

    class Meta:
        abstract = True