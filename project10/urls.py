from django.contrib import admin
from django.urls import path
from formapp.views import Input, Insert

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Input.as_view()),
    path('insert', Insert.as_view()),
]