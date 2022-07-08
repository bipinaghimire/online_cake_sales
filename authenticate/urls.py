from django.urls import  path
from authenticate import views


urlpatterns = [
    path("login", (views.login_fn)),
    path("register", (views.register_fn)),
]