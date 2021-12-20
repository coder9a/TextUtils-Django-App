from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('removepunc/', views.removepunc, name='removepunc'),
    path('capitalizefirst/', views.capfirst, name='capfirst'),
    path('newlineremove/', views.newlineremove, name='newlineremove'),
    path('charcount/', views.charcount, name='charcount'),
]
