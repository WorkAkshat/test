from django.urls import path
from .views import upload_tree, success

urlpatterns = [
    path('upload/', upload_tree, name='upload_tree'),
    path('success/', success, name='success'),
]
