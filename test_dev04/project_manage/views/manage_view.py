from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from project_manage.models import Project
from project_manage.forms import my_form


@login_required  # 限制未登录状态不能进入视图
def manage(request):
    projects = Project.objects.all()  # 获取数据库值
    # accountName = request.COOKIES.get("accountName", "")  # 获取cookies
    accountName = request.session.get("accountName", "")  # 获取 session
    return render(request, 'manage2.html', {"accountName": accountName, "projects": projects})


@login_required  # 限制未登录状态不能进入视图
def project_add(request):
    """
    项目添加
    :param request:
    :return:
    """
    accountName = request.session.get("accountName", "")  # 获取 session
    if request.method == "GET":  # 不提交时返回表单
        form = my_form()  # 空的表单对象
        return render(request, "project/project_add.html", {"accountName": accountName, "form": form})  # 生产空表单对象
    elif request.method == "POST":  # 表单提交

        form = my_form(request.POST)  # 获取表单提交内容
        if form.is_valid():  # 判断 form 提交的内容是否无效
            projectName = form.cleaned_data['name']
            projectDescribe = form.cleaned_data['describe']
            projectStatus = form.cleaned_data['status']
            Project.objects.create(name=projectName, describe=projectDescribe, status=projectStatus)  # 表单数据提交数据库
            return HttpResponseRedirect('/manage/')


@login_required  # 限制未登录状态不能进入视图
def project_edit(request, pid):  # 拿到链接的参数
    """
    项目更新
    :param request:
    :param pid:
    :return:
    """
    accountName = request.session.get("accountName", "")  # 获取 session
    # 处理表单提交

    if request.method == "POST":
        # 表单已经修改了数据，提高之后更新表里面的数据
        form = my_form(request.POST)
        if form.is_valid():
            project = Project.objects.get(id=pid)
            project.name = form.cleaned_data['name']
            project.describe = form.cleaned_data['describe']
            project.status = form.cleaned_data['status']
            project.save()
            return HttpResponseRedirect('/manage/')
    else:
        # 打开编辑表单，回显数据
        if pid:
            try:
                p = Project.objects.get(id=pid)
                form = my_form(instance=p)  # 生产带数据表单
                return render(request, 'project/project_edit.html',
                              {"accountName": accountName, "form": form, 'pid': pid})
            except Project.DoesNotExist:
                return HttpResponseRedirect("/manage/")


@login_required  # 限制未登录状态不能进入视图
def project_delete(request, pid):
    if pid:
        try:
            project = Project.objects.get(id=pid)
            project.delete()
            return HttpResponseRedirect("/manage/")
        except Project.DoesNotExist:
            return HttpResponseRedirect("/manage/")
