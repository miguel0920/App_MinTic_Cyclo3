from tkinter.tix import Tree
from django.db import models

from .modelbase import ModelBase
from fedemy.models.usercompanies import UserCompanies
from fedemy.models.packagetypes import PackageTypes


class Packages(ModelBase):
    """Packages model."""
    packageid = models.BigAutoField(primary_key=True)
    usercompanyid = models.ForeignKey(UserCompanies, on_delete=models.CASCADE,
                                      null=False, blank=False,
                                      related_name='packages')
    packagetypeid = models.ForeignKey(
        PackageTypes, on_delete=models.DO_NOTHING, related_name='packagetypeid_packeage_set')
    packagedescription = models.CharField(max_length=50)
    packagetitle = models.CharField(max_length=50)
    packageprice = models.CharField(max_length=50)
    packagequantity = models.CharField(max_length=50)

    class Meta:
        db_table = "packages"
