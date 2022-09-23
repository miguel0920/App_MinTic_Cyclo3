from django.db import models

from .modelbase import ModelBase

class States(ModelBase):
    """States model."""
    stateId = models.BigAutoField(primary_key=True)
    stateName = models.CharField(max_length=255)
    stateCode = models.IntegerField()

    class Meta:
        db_table = "states"