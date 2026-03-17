
from django.http import HttpResponse
from .models import BlogPost,Like
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()  # same here
# Create your views here.
@login_required
def create_blog(request):
    if request.method=="POST":
        title=request.POST.get("title")
        content=request.POST.get("content")
        BlogPost.objects.create(title=title,content=content,author=request.user)
        messages.success(request, "Blog uploaded successfully!")
        return redirect("BlogUpload:create_blog")
        
    return render(request, "BlogUpload/write.html")

@login_required
def display_blogs(request):
    blogs = BlogPost.objects.filter(is_published=True).order_by("-created_at")
    
    context = {"blogs": blogs}
    return render(request, "BlogUpload/display.html", context)

@login_required
def profile(request):
    user=request.user
    print(user)
    blogs=BlogPost.objects.filter(author=user)
    context={"blogs":blogs,
             "user":user}
    return render(request,"BlogUpload/profile.html",context)
    
@login_required
def delete_account(request):
    user = request.user
    user.delete()
    messages.success(request, "Your account has been deleted.")
    return redirect("accounts:register")

@login_required
def edit_blog(request,blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    if blog.author != request.user:
        return redirect("BlogUpload:display_blogs")
    if request.method=="POST":
        title=request.POST.get("title")
        content=request.POST.get("content")
        blog.title=title
        blog.content=content
        blog.created_at = timezone.now()
        blog.save()
        messages.success(request, "Blog updated successfully!")
        return redirect("BlogUpload:profile")
    context={"blog":blog}
    return render(request,"BlogUpload/edit_blog.html",context)


@login_required
def delete_blog(request,blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    if blog.author != request.user:
        return redirect("BlogUpload:display_blogs")
    blog.delete()
    messages.success(request, "Blog deleted successfully!")
    return redirect("BlogUpload:profile")


def likeBlog(request,blog_id):
    post=get_object_or_404(BlogPost, id=blog_id)
    like_alread_exit=Like.objects.filter(user=request.user, post=post).exists()
    if like_alread_exit:
        like_alread_exit.delete()
    else:
        Like.objects.create(user=request.user, post=post)

    return redirect("BlogUpload:display_blogs")
        
