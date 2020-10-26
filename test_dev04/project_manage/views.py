from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def hello(request):
    if request.method == 'GET':
        name = request.GET.get('name', '')
        return render(request, 'hello.html', {'name': name})


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        ps = request.POST.get('password')
        userauth = auth.authenticate(username=username, password=ps)
        if username == '' or ps == '':
            print("用户密码不为空")
            return render(request, 'index.html', {'msg': '用户密码不为空'})
        if userauth is not None:
            auth.login(request, userauth)# 登录成功，db写sessionId
            return HttpResponseRedirect('/manage/')
        else:
            return render(request, 'index.html', {'msg': '用户名密码错误'})


@login_required  # 限制未登录状态不能进入视图
def manage(request):
    return render(request, 'manage.html')


def logout(request):
    """
    登出
    :param request:
    :return:
    """
    auth.logout(request)
    # return render(request, 'index.html') # 这种返回方式 路径不会改变
    return HttpResponseRedirect("/index/")
