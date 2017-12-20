from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^categories/$', views.category_list, name='category_list'),
    url(r'^categories/$', views.CategoryList.as_view(), name=views.CategoryList.name),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view(), name=views.CategoryDetail.name),
    url(r'^posts/$', views.PostList.as_view(), name=views.PostList.name),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name=views.PostDetail.name),
    url(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
