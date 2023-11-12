from django.urls import path
from account import views

urlpatterns = [
    path('logout/',views.user_logout, name="logout"),
    path('',views.user_login, name="login"),
    path('newsfun/',views.newfun,{'template_name':'account/temp.html'},name="newfun"),
    path('newsfun1/',views.newfun,{'template_name':'account/temp1.html'},name="newfun1"),
    path('cl/',views.NewClassView.as_view(),name="cl"),
    path('cl1/',views.NewClassView1.as_view(template_name='account/temp1.html'),name="cl1"),
    path('cl2/',views.NewClassView1.as_view(template_name='account/temp.html'),name="cl2"),
]
