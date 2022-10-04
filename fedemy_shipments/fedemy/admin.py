from django.contrib import admin
from .models.user import User
from .models.cities import Cities
from .models.companies import Companies
from .models.modelbase import ModelBase
from .models.orders import Orders
from .models.ordersdetails import OrdersDetails
from .models.packages import Packages
from .models.packagetypes import PackageTypes
from .models.people import People
from .models.states import States
from .models.statesorders import StatesOrders
from .models.usercompanies import UserCompanies

# Register your models here.
admin.site.register(User)
admin.site.register(Cities)
admin.site.register(Companies)
admin.site.register(Orders)
admin.site.register(OrdersDetails)
admin.site.register(Packages)
admin.site.register(PackageTypes)
admin.site.register(People)
admin.site.register(States)
admin.site.register(StatesOrders)
admin.site.register(UserCompanies)