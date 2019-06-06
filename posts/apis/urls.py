from django.urls import path
from .views import PostSerializerViewList


urlpatterns = [
    path('',PostSerializerViewList.as_view(),name="api-post-list")
]