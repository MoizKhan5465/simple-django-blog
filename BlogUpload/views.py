
from django.http import HttpResponse
from .models import BlogPost
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
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


def display_blogs(request):
    blogs = BlogPost.objects.filter(is_published=True).order_by("-created_at")
    context = {"blogs": blogs}
    return render(request, "BlogUpload/display.html", context)
def home(request):
    return HttpResponse("Hello, World! This is the home page of the BlogUpload app.")