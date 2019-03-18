from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'colony', views.ColonyViewSet)
router.register(r'oxxos', views.OxxoViewSet)


urlpatterns = []
urlpatterns += router.urls
