from django.urls import path
from case_manage import views

urlpatterns = [
    # path("project_add/", project_manage_view.project_add),
    path("case_list/", views.case_list),
    path("case_save/", views.case_save),
    # path("case_postman/", views.case_postman),
    path("case_edit/<int:cid>/", views.case_edit),
    path("case_delete/", views.case_delete),
    path("case_edit_save/", views.case_edit_save),

]
