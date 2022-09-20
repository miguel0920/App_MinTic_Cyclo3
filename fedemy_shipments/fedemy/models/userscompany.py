from django.db import models

from fedemy.models.companies import Companies
from fedemy.models.user import User
from fedemy.models.people import People

from .modelbase import ModelBase

class UsersCompanies(ModelBase):
    """UsersCompanies model."""
    companyId = models.ForeignKey(Companies, on_delete=models.DO_NOTHING, related_name='companies')
    id = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='fedemy_user')
    personId = models.ForeignKey(People, on_delete=models.DO_NOTHING, related_name='people')

    class Meta:
        db_table = "userscompanies"