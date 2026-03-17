from BlogUpload import views
from django.urls import path,include

app_name = "BlogUpload"
urlpatterns = [
    
    path("",views.create_blog,name="create_blog"),
    path("display/",views.display_blogs,name="display_blogs"),
    path("profile/",views.profile,name="profile"),
    path("delete_account/",views.delete_account,name="delete_account"),
    path("edit_blog/<int:blog_id>/",views.edit_blog,name="edit_blog"),
    path("delete_blog/<int:blog_id>/",views.delete_blog,name="delete_blog"),
    path("like/<int:blog_id>/",views.likeBlog,name="likeBlog"),
    path("comment/<int:blog_id>/",views.commentBlog,name="commentBlog"),

]