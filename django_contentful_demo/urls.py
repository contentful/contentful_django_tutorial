"""django_contentful_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
#from django.contrib import admin
from frontend import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^blog$', views.blogs),
    url(r'^blog/(?P<slug>[-\w]+)$', views.blog_by_slug),
    url(r'^projects$', views.projects),
    url(r'^projects/(?P<slug>[-\w]+)$', views.project_by_slug),
]
