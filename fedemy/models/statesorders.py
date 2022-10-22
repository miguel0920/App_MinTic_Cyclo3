from django.db import models

from .modelbase import ModelBase


class StatesOrders(ModelBase):
    """StatesOrders model."""
    stateorderid = models.IntegerField(
        primary_key=True, db_column='stateorderid')
    stateordername = models.CharField(
        max_length=50, db_column='stateordername')

    class Meta:
        db_table = "statesorders"
