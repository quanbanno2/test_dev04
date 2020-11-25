from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from project_manage.models import Module
from project_manage.forms import module_form


@login_required  # 限制未登录状态不能进入视图
def manage(request):
    module = Module.objects.all()  # 获取数据库值
    accountName = request.session.get("accountName", "")  # 获取 session
    return render(request, 'module/module_manage.html', {"accountName": accountName, "modules": module})


@login_required  # 限制未登录状态不能进入视图
def module_add(request):
    """
    项目添加
    :param request:
    :return:
    """
    accountName = request.session.get("accountName", "")  # 获取 session
    if request.method == "GET":  # 不提交时返回表单
        form = module_form()  # 空的表单对象
        return render(request, "module/module_add.html", {"accountName": accountName, "form": form})  # 生产空表单对象
    elif request.method == "POST":  # 表单提交
        form = module_form(request.POST)  # 获取表单提交内容
        if form.is_valid():  # 判断 form 提交的内容是否无效
            moduleName = form.cleaned_data['name']
            moduleDescribe = form.cleaned_data['describe']
            moduleProject = form.cleaned_data['project']
            Module.objects.create(name=moduleName, describe=moduleDescribe, project=moduleProject)  # 表单数据提交数据库
            return HttpResponseRedirect('/manage/module/')


@login_required  # 限制未登录状态不能进入视图
def module_edit(request, mid):  # 拿到链接的参数
    """
    mk更新
    :param request:
    :param mid:
    :return:
    """
    accountName = request.session.get("accountName", "")  # 获取 session
    # 处理表单提交
    if request.method == "POST":
        # 表单已经修改了数据，提高之后更新表里面的数据
        form = module_form(request.POST)
        if form.is_valid():
            module = Module.objects.get(id=mid)
            module.name = form.cleaned_data['name']
            module.describe = form.cleaned_data['describe']
            module.project = form.cleaned_data['project']
            module.save()
            return HttpResponseRedirect('/manage/module/')
    else:
        # 打开编辑表单，回显数据
        if mid:
            try:
                mod = Module.objects.get(id=mid)
                form = module_form(instance=mod)  # 生产带数据表单
                return render(request, 'module/module_edit.html',
                              {"accountName": accountName, "form": form, 'pid': mid})
            except Module.DoesNotExist:
                return HttpResponseRedirect("/manage/module/")


@login_required  # 限制未登录状态不能进入视图
def module_delete(request, mid):
    if mid:
        try:
            module = Module.objects.get(id=mid)
            module.delete()
            return HttpResponseRedirect("/manage/module/")
        except Module.DoesNotExist:
            return HttpResponseRedirect("/manage/module/")
