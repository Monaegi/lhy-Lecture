from django.urls import include, path
from rest_framework.routers import DefaultRouter

from courses.apis import SectionViewSet

router = DefaultRouter()
router.register(r'section', SectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
