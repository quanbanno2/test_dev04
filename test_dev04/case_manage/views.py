from django.shortcuts import render

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required  # 限制未登录状态不能进入视图
def case_list(request):
    return render(request, "case/postman.html")

# @login_required  # 限制未登录状态不能进入视图
# def case_add(request):
