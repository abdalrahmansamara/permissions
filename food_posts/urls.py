from django.urls import path
from .views import PostDetailsView, PostsListView

urlpatterns = [
    path('', PostsListView.as_view(), name='posts_api'),
    path('/<int:pk>', PostDetailsView.as_view(), name='post_details_api'),
]