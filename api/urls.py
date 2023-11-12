from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api import views
from rest_framework.routers import DefaultRouter
from .viewsets import StudentModelViewSet,ClassRoomModelViewSet

router= DefaultRouter()
router.register('student', StudentModelViewSet, basename="student"),
router.register('classroom', ClassRoomModelViewSet, basename="classroom")

urlpatterns=[
    path('helo/', views.hello_api,name="helo"),
    path('info/',views.info_api.as_view(),name="info"),
    path("stu/<int:id>/",views.StudentView.as_view()),
    path("stu_list/",views.StudentListView.as_view()),
    path('student-view/<int:id>/',views.StudentAPiView.as_view()),
    path('stu-listcreateview/',views.StudentListCreateView.as_view()),
    path('stud-list-create/',views.StudentAPiView.as_view()),
    path('stu-create-view/',views.StudentCreateGenericView.as_view()),
    path('stu-listcreate/',views.StudentListCreateGenericView.as_view()),
    path('stu-retrive/<int:pk>/',views.StudentRetriveGenericView.as_view()),
    path('stu-update/<int:pk>/',views.StudentUpdateGenericView.as_view()),
    path('stu-delete/<int:pk>/',views.StudentDeleteGenericView.as_view()),
    path('stu-re-up-de/<int:pk>/',views.StudentREUPDeGenericView.as_view()),
    path('login/',obtain_auth_token, name="token_login")

] + router.urls