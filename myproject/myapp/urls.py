from django.urls import path
from .views import Deptview , Empview
urlpatterns = [
    path('dept/', Deptview.as_view(), name='dept'),
    path('emp/', Empview.as_view(), name='emp'),
]