from django.db import models

from .modelbase import ModelBase

class People(ModelBase):
    """People model."""
    personId = models.BigAutoField(primary_key=True)
    personFirstName = models.CharField(max_length=50)
    personSecondName = models.CharField(max_length=50)
    personLastName = models.CharField(max_length=50)
    personSecondLastName = models.CharField(max_length=50)
    personAddress = models.CharField(max_length=50)
    personPhone = models.CharField(max_length=50)
    personEmail = models.CharField(max_length=50)

    class Meta:
        db_table = "people"