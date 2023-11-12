"""
URL configuration for myproject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth import decorators

urlpatterns = [
    path('admin/', admin.site.urls),
    path('port/', views.port, name="port"),
    path('test/', views.test, name="test"),
    path('page1/', views.page1, name="page1"),
    path('page2/', views.page2, name="page2"),
    path('stu/', views.class_info, name="stu"),
    path('stuform/', views.studentform,name="stuform"),
    path('api/',include("api.urls")),
    path('',include("account.urls")),
    path('form/', include("form.urls")),
    path('', views.home, name="home"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)