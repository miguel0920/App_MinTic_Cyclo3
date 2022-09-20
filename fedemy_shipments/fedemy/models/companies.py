from django.db import models

from .modelbase import ModelBase

class Companies(ModelBase):
    """Companies model."""
    companyName = models.CharField(max_length=50)
    companyAddress = models.CharField(max_length=50)
    companyPhone = models.CharField(max_length=50)

    class Meta:
        db_table = "companies"