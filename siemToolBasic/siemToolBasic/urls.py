"""
URL configuration for siemToolBasic project.

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
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path(r'^output', views.calc,name="scriptforbtnPress"),
    #path('dashboard', views.dashboardPage,name="dashboardP"),
    path('security', views.securityPage,name="securityP"),
    path('system', views.systemPage,name="systemP"),
    path('application', views.applicationPage,name="applicationP"),
]
