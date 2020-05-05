
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework import routers
from department.views import DepartmentViewSet

router = routers.DefaultRouter()
router.register(r'department', DepartmentViewSet)
# router.register(r'babies', BabyViewSet)
# router.register(r'babies', BabyViewSet)
# router.register(r'babies', BabyViewSet)
# router.register(r'babies', BabyViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls))
]
