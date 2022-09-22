from django.db import models

from .modelbase import ModelBase
from fedemy.models.usercompanies import UserCompanies
from fedemy.models.statesorders import StatesOrders

class Orders(ModelBase):
    """Orders model."""
    orderId = models.BigAutoField(primary_key=True)
    userCompanyId = models.ForeignKey(UserCompanies, on_delete=models.DO_NOTHING, related_name='usercompanyid_orders_set')
    stateOrderId = models.ForeignKey(StatesOrders, on_delete=models.DO_NOTHING, related_name='stateOrderId_orders_set')
    orderNumber = models.CharField(max_length=100)
    orderTotal = models.DecimalField(max_digits=5, decimal_places=2)
    orderDateDelivery = models.DateField()

    class Meta:
        db_table = "orders"