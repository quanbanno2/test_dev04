from django.urls import path
from api_manage import views

urlpatterns = [
    path("v1/debug/", views.debug),

]
