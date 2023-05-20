from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


app_name = 'api'

router = SimpleRouter()
router.register(r'v1/posts', PostViewSet)
router.register(
    r'v1/posts/(?P<post>[\d]+)/comments', CommentViewSet, basename='comments'
)
router.register(r'v1/follow', FollowViewSet, basename='follows')
router.register(r'v1/groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
