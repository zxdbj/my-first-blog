from django.urls import path

from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
]



# from django.conf.urls import url
# from . import views

# urlpatterns = [
#     url(r'^$', views.post_list, name='post_list'),
# ]