from django.urls import path
from .views import Deptview , Empview , EmpUpdation
urlpatterns = [
    path('dept/', Deptview.as_view(), name='dept'),
    path('emp/', Empview.as_view(), name='emp'),
    path('emp/<int:emp_id>/' , EmpUpdation.as_view(), name='EmpUpdation')
]