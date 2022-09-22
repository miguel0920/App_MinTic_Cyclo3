from django.db import models

from .modelbase import ModelBase
from fedemy.models.states import States

class Cities(ModelBase):
    """Cities model."""
    cityid = models.BigAutoField(primary_key=True)
    stateid = models.ForeignKey(States, on_delete=models.DO_NOTHING, related_name='stateid_states_set')
    citycode = models.IntegerField()
    cityname = models.CharField(max_length=255)

    class Meta:
        db_table = "cities"