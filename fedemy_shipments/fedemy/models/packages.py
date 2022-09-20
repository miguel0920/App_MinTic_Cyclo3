from django.db import models

from .modelbase import ModelBase
from fedemy.models.userscompany import UsersCompanies
from fedemy.models.packagetypes import PackageTypes

class Packages(ModelBase):
    """Packages model."""
    usercompanyId = models.ForeignKey(UsersCompanies, on_delete=models.DO_NOTHING, related_name='userscompanies')
    packageTypeId = models.ForeignKey(PackageTypes, on_delete=models.DO_NOTHING, related_name='packageTypes')
    packageEmail = models.CharField(max_length=50)
    packageTypeId = models.CharField(max_length=50)
    packageDescription = models.CharField(max_length=50)
    packageTitle = models.CharField(max_length=50)
    packagePrice = models.CharField(max_length=50)
    packageQuantity = models.CharField(max_length=50)

    class Meta:
        db_table = "packages"