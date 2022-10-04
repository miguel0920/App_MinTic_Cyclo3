from django.db import models

from .modelbase import ModelBase


class States(ModelBase):
    """States model."""
    stateid = models.IntegerField(primary_key=True, db_column='stateid')
    statename = models.CharField(max_length=50, db_column='statename')
    statecode = models.IntegerField(db_column='statecode')

    class Meta:
        db_table = "states"
