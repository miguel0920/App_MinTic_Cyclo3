from django.db import models

from .modelbase import ModelBase

class UserCustomersType(ModelBase):
    """People model."""
    userCustomerTypeId = models.BigAutoField(primary_key=True)
    userCustomerTypeName = models.CharField(max_length=50)

    class Meta:
        db_table = "usercustomerstype"