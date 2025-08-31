from django.urls import path
from .views import Deptview
urlpatterns = [
    path('dept/', Deptview.as_view(), name='dept'),
]