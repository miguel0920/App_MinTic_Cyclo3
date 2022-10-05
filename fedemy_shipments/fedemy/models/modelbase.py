from django.db import models
import datetime


class ModelBase(models.Model):
    createdatetime = models.DateField(
        db_column='createdatetime')
    updatedatetime = models.DateField(
        null=True, db_column='updatedatetime')
    isactive = models.BooleanField(db_column='isactive')

    class Meta:
        abstract = True
