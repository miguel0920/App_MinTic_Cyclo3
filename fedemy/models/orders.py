from django.db import models

from .modelbase import ModelBase
from fedemy.models.usercompanies import UserCompanies
from fedemy.models.statesorders import StatesOrders
from fedemy.models.people import People
from fedemy.models.cities import Cities


class Orders(ModelBase):
    """Orders model."""
    orderid = models.IntegerField(primary_key=True, db_column='orderid')
    usercompanyid = models.ForeignKey(
        UserCompanies, on_delete=models.DO_NOTHING, related_name='usercompanyid_orders_set', db_column='usercompanyid')
    stateorderid = models.ForeignKey(
        StatesOrders, on_delete=models.DO_NOTHING, related_name='stateOrderId_orders_set', db_column='stateorderid')
    ordernumber = models.CharField(max_length=100, db_column='ordernumber')
    ordertotal = models.DecimalField(
        max_digits=5, decimal_places=2, db_column='orderTotal')
    orderdatedelivery = models.DateField(
        db_column='orderdatedelivery', null=True)
    personsenderid = models.ForeignKey(
        People, on_delete=models.DO_NOTHING, related_name='personsenderid_orders_set', db_column='personsenderid')
    personreceiverid = models.ForeignKey(
        People, on_delete=models.DO_NOTHING, related_name='personreceiverid_orders_set', db_column='personreceiverid')
    cityid = models.ForeignKey(Cities, on_delete=models.DO_NOTHING,
                               related_name='cityid_orders_set', db_column='cityid')
    usercreate = models.IntegerField(db_column='usercreate')
    userupdate = models.IntegerField(null=True, db_column='userupdate')

    class Meta:
        db_table = "orders"
