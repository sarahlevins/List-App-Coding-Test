"""listapp URL Configuration

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
from django.urls import path
from tennis.views import PlayerList, PlayerDetail, PlayerAdd, PlayerDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PlayerList.as_view(), name='home'),
    path('<int:pk>/', PlayerDetail.as_view(), name='detail-player',),
    path('add_player/', PlayerAdd.as_view(), name='add-player'),
    path('<int:pk>/delete_player/', PlayerDelete.as_view(), name='delete-player')
]
