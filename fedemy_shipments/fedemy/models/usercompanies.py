from django.db import models

from fedemy.models.companies import Companies
from fedemy.models.user import User
from fedemy.models.people import People

from .modelbase import ModelBase


class UserCompanies(ModelBase):
    """UserCompanies model."""
    usercompanyid = models.BigAutoField(primary_key=True)
    companyid = models.ForeignKey(Companies, on_delete=models.CASCADE,
                                  null=False, blank=False,
                                  related_name='usercompanies')
    id = models.ForeignKey(User, on_delete=models.CASCADE,
                           related_name='fedemy_user')
    userId = models.ForeignKey(
        People, on_delete=models.CASCADE, related_name='personid_people_set')

    class Meta:
        db_table = "usercompanies"
