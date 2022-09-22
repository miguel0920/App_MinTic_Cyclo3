from django.db import models

from .modelbase import ModelBase

class StatesOrders(ModelBase):
    """StatesOrders model."""
    stateOrderId = models.BigAutoField(primary_key=True)
    stateOrderName = models.CharField(max_length=50)

    class Meta:
        db_table = "statesorders"