"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from gallery.views import Gallery_views,Image_views,AddUser,LoginView,GalleryListView,HomeView,ImageListView,ImageListView2,IndexView
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    url(r'home/', HomeView.as_view(), name='home'),
	url(r'gallery/', Gallery_views.as_view(), name='gallery'),
	url(r'image/', Image_views.as_view(), name='images'),
	url(r'signup/', AddUser.as_view(), name='signup'),
    url(r'login/',LoginView.as_view(), name='login'),
    url(r'gallerylist/', GalleryListView.as_view(), name = 'gallerylist'),
    url(r'imagelist/', ImageListView.as_view(), name = 'imagelist'),
    url(r'imagelist2/', ImageListView2.as_view(), name = 'imagelist2'),
    url(r'', IndexView.as_view(), name = 'index'),
   

    

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)