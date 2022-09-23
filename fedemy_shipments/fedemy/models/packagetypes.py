from django.db import models

from .modelbase import ModelBase

class PackageTypes(ModelBase):
    """PackageTypes model."""
    packagetypeid = models.IntegerField(primary_key=True, db_column='packagetypeid')
    packagetypename = models.CharField(max_length=50, db_column='packagetypename')

    class Meta:
        db_table = "packagetypes"