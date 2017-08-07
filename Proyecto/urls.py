from django.conf.urls import url,include
from django.contrib import admin

from rest_framework import routers
from Rest.viewsets import ProductoViewset

router = routers.DefaultRouter()
router.register(r'Productos',ProductoViewset)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^rest/', include(router.urls)),
]
