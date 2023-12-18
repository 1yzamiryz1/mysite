from django.urls import path
from blog.views import *

app_name = "blog"


urlpatterns = [
    path("", blog_view, name="blog_view"),
    path("<int:pid>", blog_single, name="single"),
]
