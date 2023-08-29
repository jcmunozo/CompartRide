"""Cicles URLs."""

# Django
from django.urls import include, path

# Django REST FrameWork
from rest_framework.routers import DefaultRouter

# views
from .views import circles as circles_views
from .views import memberships as membership_views

router = DefaultRouter()

router.register(r'circles',circles_views.CircleViewSet, basename='circle')
router.register(
    r'circles/(?P<slug_name>[-a-zA-Z0-0_]*)/members',
    membership_views.MembershipViewSet,
    basename='membership'
)

urlpatterns = [
    path('', include(router.urls))
]

