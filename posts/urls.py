from django.urls import path
from .views import PostList, post_like, post_hate, filtering, author_posts, newPostView, homeView


urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<pk>/like', post_like, name="post-like"),
    path('<pk>/hate', post_hate, name="post-hate"),
    path('filtering', filtering, name="filter"),
    path('<author>', author_posts, name="filtername"),
    path('', newPostView, name='newPost'),
    path('', homeView, name='home')
]
