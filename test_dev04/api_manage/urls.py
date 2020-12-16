from django.urls import path
from api_manage import views

urlpatterns = [
    path("v1/debug/", views.debug),
    path("req/", views.req),
    path("assertResult/", views.assertResult),
    path("get_case_info/<int:cid>/", views.get_case_info),
    path("select_data/", views.select_data),

]
