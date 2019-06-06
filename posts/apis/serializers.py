from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =['title','content','likes','hates','timestamp','number_of_likes','number_of_hates']