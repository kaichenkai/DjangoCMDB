"""cmdb URL Configuration

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

from django.conf.urls import url, include
from django.contrib import admin

import async_tasks.urls
import users.urls
import business.urls
import repository.urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),  # django 默认包含的

    # 包含子路由
    url(r"^users/", include(users.urls)),
    url(r"^business/", include(business.urls)),
    url(r"^async_tasks/", include(async_tasks.urls)),
    url(r"^repository/", include(repository.urls)),
]
