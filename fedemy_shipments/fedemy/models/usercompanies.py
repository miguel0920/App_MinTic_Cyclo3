from django.db import models

from fedemy.models.companies import Companies
from fedemy.models.user import User
from fedemy.models.people import People

from .modelbase import ModelBase


class UserCompanies(ModelBase):
    """UserCompanies model."""
    usercompanyid = models.IntegerField(
        primary_key=True, db_column='usercompanyid')
    companyid = models.ForeignKey(Companies, on_delete=models.CASCADE,
                                  null=False, blank=False,
                                  related_name='usercompanies',
                                  db_column='companyid')
    fedemy_userid = models.ForeignKey(User, on_delete=models.CASCADE,
                                      related_name='fedemy_user', db_column='fedemy_userid')
    personid = models.ForeignKey(
        People, on_delete=models.CASCADE, related_name='People', db_column='personid')

    class Meta:
        db_table = "usercompanies"
