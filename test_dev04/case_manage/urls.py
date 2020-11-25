from django.urls import path
from case_manage import views

urlpatterns = [
    # path("project_add/", project_manage_view.project_add),
    path("", views.case_list),
    # path("project_edit/<int:pid>/", project_manage_view.project_edit),  # 匹配project_edit后的整数
    # path("project_delete/<int:pid>/", project_manage_view.project_delete),  # 匹配project_edit后的整数
    #
    # path("module/", module_manage_view.manage),
    # path("module_add/", module_manage_view.module_add),
    # path("module_edit/<int:mid>/", module_manage_view.module_edit),
    # path("module_delete/<int:mid>/", module_manage_view.module_delete),

]
