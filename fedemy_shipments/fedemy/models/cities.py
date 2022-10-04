from django.db import models

from .modelbase import ModelBase
from fedemy.models.states import States


class Cities(ModelBase):
    """Cities model."""
    cityid = models.IntegerField(primary_key=True, db_column='cityid')
    stateid = models.ForeignKey(
        States, on_delete=models.DO_NOTHING, related_name='stateid_states_set', db_column='stateid')
    citycode = models.IntegerField(db_column='citycode')
    cityname = models.CharField(max_length=255, db_column='cityname')

    class Meta:
        db_table = "cities"
