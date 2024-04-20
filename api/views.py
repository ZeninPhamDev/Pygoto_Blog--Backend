from rest_framework import generics

from blog.models import Post

from .serializers import PostSerializer

from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly

class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
    

class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

""" Concrete View Classes
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
Provides a get method handler.

#CreateAPIView
Used for create-only endpoints.
Provides a post method handler

#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
Provides a get method handler.

#UpdateAPIView
Used for update-only endpoints for a single model instance.
Provides put and patch method handlers.

#DestroyAPIView
Used for delete-only endpoints for a single model instance.
Provides a delete method handler.

...
"""

