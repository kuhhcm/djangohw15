from django.contrib import admin
from django.urls import path
from app.views import BookListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BookListView.as_view(), name="home"),
]