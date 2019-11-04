"""aaryanindustries URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.apps import apps


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    #url(r'^i18n/', include('django.conf.urls.i18n')),
    path('i18n/', include('django.conf.urls.i18n')),  # > Django-2.0

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.

    #url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls),  # > Django-2.0

    #url(r'^', include(apps.get_app_config('oscar').urls[0])),
    path('', include(apps.get_app_config('oscar').urls[0])),  # > Django-2.0
]