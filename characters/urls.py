from rest_framework.routers import DefaultRouter
from .views import CharacterViewSet, LocationViewSet, EpisodeViewSet
router = DefaultRouter()
router.register('character', CharacterViewSet)
router.register('location', LocationViewSet)
router.register('episode', EpisodeViewSet)

urlpatterns = router.urls