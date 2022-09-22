from django.db import models

from .modelbase import ModelBase
from fedemy.models.packages import Packages
from fedemy.models.orders import Orders

class OrdersDetails(ModelBase):
    """OrdersDetails model."""
    orderDetailId = models.BigAutoField(primary_key=True)
    packageId = models.ForeignKey(Packages, on_delete=models.DO_NOTHING, related_name='packageid_ordersdetails_set')
    orderId = models.ForeignKey(Orders, on_delete=models.DO_NOTHING, related_name='orderid_ordersdetails_set')
    orderDetailQuantity = models.IntegerField()
    orderDetailPrice = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        db_table = "ordersdetails"