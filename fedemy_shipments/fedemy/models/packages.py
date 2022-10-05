from django.db import models

from .modelbase import ModelBase
from fedemy.models.usercompanies import UserCompanies
from fedemy.models.packagetypes import PackageTypes


class Packages(ModelBase):
    """Packages model."""
    packageid = models.BigIntegerField(primary_key=True, db_column='packageid')
    usercompanyid = models.ForeignKey(UserCompanies, on_delete=models.CASCADE,
                                      null=False, blank=True,
                                      db_column='usercompanyid')
    packagetypeid = models.ForeignKey(
        PackageTypes, on_delete=models.CASCADE, related_name='packagetypeid_packeage_set',
        db_column='packagetypeid')
    packagedescription = models.CharField(
        max_length=50, db_column='packagedescription')
    packageprice = models.DecimalField(
        max_digits=11, decimal_places=2, db_column='packageprice')
    packagequantity = models.IntegerField(db_column='packagequantity')

    class Meta:
        db_table = "packages"
