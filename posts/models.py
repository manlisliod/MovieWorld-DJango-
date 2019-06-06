from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Count

user = get_user_model()

class PostManager(models.Manager):
    def filtering(self,request):
        filterer_likes=request.GET.get('likes')
        filterer_hates = request.GET.get('hates')
        filterer_date = request.GET.get('dateselect')        
        # if len(request.GET)>=1:
        #     for i in request.GET.keys():
        #         if request.GET.get(i) == "Ascending":
        #             print(request.GET.values())
                    
        #             return simple_stort(object=request.GET.get(i))
        #         else:
        #             return simple_stort(value="Desc",object=request.GET.keys().index(i))
        if filterer_likes:
            if filterer_likes=="Ascending":
                return simple_stort(value="Ascending",obj='likes')
            else:
                return simple_stort(value="Desc",obj='likes')
        if filterer_hates:
            if filterer_hates=="Ascending":
                return simple_stort(value="Ascending",obj='hates')
            else:
                return simple_stort(value="Desc",obj='hates')
        if filterer_date:
            if filterer_date=="Ascending":
                return simple_stort(value="Ascending",obj='timestamp')
            else:
                return simple_stort(value="Desc",obj='timestamp')
        return Post.objects.all()
        

def simple_stort(value="Ascending",obj=None,*args,**kwargs):
            if value=="Ascending":
                return Post.objects.annotate(num=Count(obj)).order_by("num")
            else:
                return Post.objects.annotate(num=Count(obj)).order_by("-num")



class Post(models.Model):
    author = models.ForeignKey(user,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    likes = models.ManyToManyField(user,related_name="liked_by")
    hates = models.ManyToManyField(user,related_name="hated_by")
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = PostManager()

    def __str__(self):
        return self.title

    @property
    def number_of_likes(self):
        return len(list(self.likes.all()))
    
    
    @property
    def number_of_hates(self):
        return self.hates.all().count()
    