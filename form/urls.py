from django.urls import path
# from .views import template_form
from form import views
from django.contrib.auth.decorators import login_required

urlpatterns=[
    path('', views.template_form, name="template_form"),
    path('student_detail/<int:id>/',views.student_detail,name="student_detail"),
    path('student_update/<int:id>/',views.student_update,name="student_update"),
    path('student_form/', views.student_form, name="student_form"),
    path('student_modelform/',views.student_modelform, name="student_modelform"),
    path('student_create/', login_required(views.StudentCreateView.as_view()), name="student_create"),
    path('student_template/',views.StudentCreateView.as_view(),name="student_template"),
    # path('student_list/',login_required(views.StudentListView.as_view()),name="student_list")
    path('student_list/',login_required(views.StudentListView.as_view()),name="student_list")
]