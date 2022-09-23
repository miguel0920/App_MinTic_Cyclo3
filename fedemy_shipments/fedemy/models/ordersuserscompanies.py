from django.db import models

from .modelbase import ModelBase
from fedemy.models.people import People
from fedemy.models.userscustomerstype import UserCustomersType
from fedemy.models.cities import Cities
from fedemy.models.orders import Orders

class OrderUserCustomer(ModelBase):
    """People model."""
    orderUserCustomerId = models.BigAutoField(primary_key=True)
    userId = models.ForeignKey(People, on_delete=models.DO_NOTHING, related_name='people')
    orderUserCustomerTypeId = models.ForeignKey(UserCustomersType, on_delete=models.DO_NOTHING, related_name='usercustomerstype')
    orderId = models.ForeignKey(Orders, on_delete=models.DO_NOTHING, related_name='orders')
    cityId = models.ForeignKey(Cities, on_delete=models.DO_NOTHING, related_name='cities')

    class Meta:
        db_table = "orderusercustomer"