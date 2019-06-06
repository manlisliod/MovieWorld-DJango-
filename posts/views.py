from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView
# Create your views here.
from .models import Post


class PostList(ListView):
    template_name='posts/post-list.html'

    def get_queryset(self):
        return Post.objects.all()

def post_like(request,pk):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=pk)
        if request.user!=post.author:
            if not request.user in post.likes.all():
                if request.user in post.hates.all():
                    post.hates.remove(request.user)
                post.likes.add(request.user)
            else:
                post.likes.remove(request.user)
        return redirect('post-list')

def post_hate(request,pk):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=pk)
        if request.user!=post.author:
            if not request.user in post.hates.all():
                if request.user in post.likes.all():
                    post.likes.remove(request.user)
                post.hates.add(request.user)
            else:
                post.hates.remove(request.user)
        return redirect('post-list')

def filtering(request):
    print(request.GET)
    r = request.GET
    if len(r)<3:
       query= Post.objects.filtering(request)
    return render(request,"posts/post-list.html",{'object_list':query})

def author_posts(request,author):
    print(author)
    query = Post.objects.all().filter(author__username=author)
    return render(request,"posts/post-list.html",{'object_list':query})

def newPostView(request):
    if request.method=="POST":
        print(request.POST.get('title'))
        Post.objects.create(title=request.POST.get('title'),content = request.POST.get('content'))
        return redirect('post-list')
    print(request)
    return redirect('post-list')

def homeView(request):
    return redirect('post-list')
