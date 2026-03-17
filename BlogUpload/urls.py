from BlogUpload import views
from django.urls import path,include

app_name = "BlogUpload"
urlpatterns = [
    
    path("",views.create_blog,name="create_blog"),
    #path("create/",views.create_blog,name="create_blog"),
    path("display/",views.display_blogs,name="display_blogs"),
    path("profile/",views.profile,name="profile"),

]