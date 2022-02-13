from django.urls import path
from django.contrib import admin
from catalog import views
#from django.conf.urls import url
from django.urls.conf import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    url(r'^books/$', views.BookListViews.as_view(), name='books')
]
