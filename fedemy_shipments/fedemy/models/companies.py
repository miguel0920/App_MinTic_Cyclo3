from django.db import models

from .modelbase import ModelBase

class Companies(ModelBase):
    """Companies model."""
    companyid = models.BigAutoField(primary_key=True)
    companyname = models.CharField(max_length=50)
    companyaddress = models.CharField(max_length=50)
    companyphone = models.CharField(max_length=50)

    class Meta:
        db_table = "companies"