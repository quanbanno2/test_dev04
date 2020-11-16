from django.urls import path
from project_manage.views import manage_view

urlpatterns = [
    path("project_add/", manage_view.project_add),
    path("", manage_view.manage),
    path("project_edit/<int:pid>/", manage_view.project_edit),  # 匹配project_edit后的整数
    path("project_delete/<int:pid>/", manage_view.project_delete),  # 匹配project_edit后的整数

]
