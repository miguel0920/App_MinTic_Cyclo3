from django.db import models

from .modelbase import ModelBase
from fedemy.models.packages import Packages
from fedemy.models.orders import Orders


class OrdersDetails(ModelBase):
    """OrdersDetails model."""
    orderdetailid = models.IntegerField(
        primary_key=True, db_column='orderdetailid')
    packageid = models.ForeignKey(
        Packages, on_delete=models.DO_NOTHING, related_name='packageid_ordersdetails_set', db_column='packageid')
    orderid = models.ForeignKey(
        Orders, on_delete=models.DO_NOTHING, related_name='orderid_ordersdetails_set', db_column='orderid')
    orderdetailquantity = models.IntegerField(db_column='orderdetailquantity')
    orderdetailprice = models.DecimalField(max_digits=11, decimal_places=2, db_column='orderdetailprice')

    class Meta:
        db_table = "ordersdetails"
