from django.db import models
import datetime


class ModelBase(models.Model):
    createdatetime = models.DateTimeField(
        db_column='createdatetime')
    updatedatetime = models.DateTimeField(
        null=True, db_column='updatedatetime')
    isactive = models.BooleanField(db_column='isactive')

    class Meta:
        abstract = True
