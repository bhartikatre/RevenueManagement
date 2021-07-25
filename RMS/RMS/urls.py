"""RMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include,path
from revenue.views import RevenueList,Details,UpdateRev,CreateRev


urlpatterns = [
    path('admin/', admin.site.urls),
    path('revenue/',RevenueList.as_view(),name='revenue'),
    path('revenue/<int:pk>',Details.as_view(),name='detail_rev'),
    path('revenue/<int:pk>/update',UpdateRev.as_view(),name='update_rev'),
    path('revenue/create',CreateRev.as_view(),name='create_rev'),
    #path('revenue/details',revenue),
    #path('revenue/update',revenue),
    #path('revenue/delete',revenue),
    #path('movies',re,name='movies')
]
