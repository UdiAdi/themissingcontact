from django.urls import path
from firstapp import views

urlpatterns = [
    path(r'', views.MembersList.as_view(), name="members_list"),
   ]
