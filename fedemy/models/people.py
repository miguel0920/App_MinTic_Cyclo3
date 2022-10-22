from django.db import models

from .modelbase import ModelBase


class People(ModelBase):
    """People model."""
    personid = models.AutoField(primary_key=True, db_column='personid')
    personfirstname = models.CharField(
        max_length=50, db_column='personfirstname')
    personsecondname = models.CharField(
        max_length=50, null=True, db_column='personsecondname')
    personlastname = models.CharField(
        max_length=50, db_column='personlastname')
    personrsecondlastname = models.CharField(
        max_length=50, db_column='personrsecondlastname')
    personaddress = models.CharField(max_length=50, db_column='personaddress')
    personphone = models.CharField(max_length=50, db_column='personphone')
    personemail = models.CharField(max_length=50, db_column='personemail')
    persondocumentnumber = models.CharField(
        max_length=50, db_column='persondocumentnumber')

    class Meta:
        db_table = "people"
