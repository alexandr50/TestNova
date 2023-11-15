
from django.urls import path, include

from .views import FileCreateView
from .apps import FileConfig

app_name = FileConfig.name

urlpatterns = [
    path('create', FileCreateView.as_view(), name='create_view')
]
