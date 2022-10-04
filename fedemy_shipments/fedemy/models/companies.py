from django.db import models

from .modelbase import ModelBase


class Companies(ModelBase):
    """Companies model."""
    companyid = models.IntegerField(primary_key=True, db_column='companyid')
    companyname = models.CharField(max_length=50, db_column='companyname')
    companyaddress = models.CharField(
        max_length=50, db_column='companyaddress')
    companyphone = models.CharField(max_length=50, db_column='companyphone')

    class Meta:
        db_table = "companies"
