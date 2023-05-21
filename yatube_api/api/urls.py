from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


app_name = 'api'

routerv1 = SimpleRouter()
routerv1.register('v1/posts', PostViewSet)
routerv1.register(
    r'v1/posts/(?P<post>[\d]+)/comments', CommentViewSet, basename='comments'
)
routerv1.register('v1/follow', FollowViewSet, basename='follows')
routerv1.register('v1/groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('', include(routerv1.urls)),
]
