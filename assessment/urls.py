"""assessment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from octotest import views
from django.conf import settings
from django.conf.urls.static import static
from octotest.views import HomePageView, SearchView, SearchResults

urlpatterns = [
    path('admin/', admin.site.urls, name="admin_page"),
    path('', HomePageView.as_view(), name="home_page"),
    path('index/',views.index, name="index"),
    path('upclean/', views.upclean, name="upclean"),
    path('search/', SearchView.as_view(), name="search"),
    path('search_results/', SearchResults.as_view(), name="search_results")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
