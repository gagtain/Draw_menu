
from django.urls import path, re_path, include
from .views import *
urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    re_path(r'^(.*)/$', index, name='index'),
    path('', index, name='index'),
]