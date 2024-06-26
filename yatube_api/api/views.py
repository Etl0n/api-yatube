from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters

from .exceptions import FollowExit
from .serializers import (
    GroupSerializer,
    FollowSerializer,
    PostSerializer,
    CommentSerializer,
)
from posts.models import Group, Follow, Post, User
from .mixins import ListCreateViewSet, RetrieveListViewSet
from .permissions import AuthorOrReadOnly, ReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        post = Post.objects.get(id=self.kwargs.get('post'))
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs.get('post'))
        serializer.save(author=self.request.user, post=post)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()


class FollowViewSet(ListCreateViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=following__username',)

    def get_queryset(self):
        follow = Follow.objects.filter(user=self.request.user)
        return follow

    def perform_create(self, serializer):
        user = User.objects.get(username=self.request.data.get('following'))
        follow = Follow.objects.filter(
            following=user, user=self.request.user
        ).exists()
        if follow or (user == self.request.user):
            raise FollowExit('Такой пост уже существует')
        serializer.save(user=self.request.user)


class GroupViewSet(RetrieveListViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
