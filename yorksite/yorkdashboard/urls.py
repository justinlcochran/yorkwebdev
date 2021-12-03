from django.urls import path

from . import views

app_name = "yorkdashboard"
urlpatterns = [
    path('', views.UserDashboard.as_view(), name="UserDashboard"),
    ]