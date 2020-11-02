from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def hello(request):
    return redirect("/index/")  # 重定向
    # name = request.body
    # print(name)
    # return HttpResponse("菜鳥教程")
    # name = request.path
    # print(name)
    # return HttpResponse("菜鸟教程")
    # if request.method == 'GET':
    #     return render(request, 'hello.html')
    # if request.method == 'POST':
    #     name = request.POST.get('firstname', '')
    #     password = request.POST.get('password', '')
    #     view_list = {"name":"tom"}
    #     return render(request, 'hello.html', {"view_list":view_list,"ps":password})


def index(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        ps = request.POST.get('password')
        userauth = auth.authenticate(username=username, password=ps)
        if username == '' or ps == '':
            return render(request, 'login.html', {'msg': '账号或密码不为空'})
        if userauth is not None:
            auth.login(request, userauth)  # 登录成功，db写sessionId
            response = HttpResponseRedirect('/manage/')
            # response.set_cookie("accountName", username, 10)  # 设置cookies
            request.session["accountName"] = username  # 设置session

            return response
        else:
            return render(request, 'login.html', {'msg': '账号或密码错误'})


# def index(request):
#     if request.method == 'GET':
#         return render(request, 'index.html')
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         ps = request.POST.get('password')
#         userauth = auth.authenticate(username=username, password=ps)
#         if username == '' or ps == '':
#             print("用户密码不为空")
#             return render(request, 'index.html', {'msg': '用户密码不为空'})
#         if userauth is not None:
#             auth.login(request, userauth)  # 登录成功，db写sessionId
#             return HttpResponseRedirect('/manage/')
#         else:
#             return render(request, 'index.html', {'msg': '用户名密码错误'})


@login_required  # 限制未登录状态不能进入视图
def manage(request):
    # accountName = request.COOKIES.get("accountName", "")  # 获取cookies
    accountName = request.session.get("accountName", "")  # 获取 session
    return render(request, 'manage2.html', {"accountName": accountName})


def logout(request):
    """
    登出
    :param request:
    :return:
    """
    auth.logout(request)
    # return render(request, 'index.html') # 这种返回方式 路径不会改变
    return HttpResponseRedirect("/index/")
