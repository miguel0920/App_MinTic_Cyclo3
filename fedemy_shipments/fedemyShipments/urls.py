"""projectAuth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from fedemy.views import UserViewSet, PackageViewSet, PeopleViewSet, PeopleListViewSet, PeopleViewSetDetail
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/users/', UserViewSet.as_view(), name='users'),
    path('api/users/create_user', UserViewSet.as_view(), name='users'),
    path('api/people/', PeopleViewSet.as_view(), name='people'),
    path('api/people/<int:pk>/', PeopleViewSetDetail.as_view(), name='people'),
    re_path('api/person/', PeopleListViewSet.as_view(), name='person'),
    path('api/packages/', PackageViewSet.as_view(), name='packages'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
