from django.db import models

from .modelbase import ModelBase

class PackageTypes(ModelBase):
    """PackageTypes model."""
    packageTypeName = models.CharField(max_length=50)

    class Meta:
        db_table = "packagetypes"