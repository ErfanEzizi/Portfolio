from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("post/<str:pk>", views.post, name='post'),
    path("posts/", views.all_posts, name='all_post'),
    path("profile/", views.profile, name='profile'),
    path("contact", views.message, name="message"),

    # crud paths
    path("create_post/", views.createPost, name="create"),
    path("update_post/<str:pk>", views.updatePost, name="update"),
    path("delete_post/<str:pk>", views.deletePost, name="delete"),

]
