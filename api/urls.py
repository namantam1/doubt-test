from django.urls import path
from .views import *

urlpatterns = [
    path('', question),
    path('name/<str:name>', question_name),
    path('date/<str:date>', question_date),
    path('type/<str:qtype>', question_type),
    path('help/',all_help),
    path('help/student',student_help),
    path('help/teacher',teacher_help)
]