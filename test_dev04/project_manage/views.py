from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from project_manage.models import Project

# def index(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         ps = request.POST.get('password')
#         userauth = auth.authenticate(username=username, password=ps)
#         if username == '' or ps == '':
#             return render(request, 'login.html', {'msg': '账号或密码不为空'})
#         if userauth is not None:
#             auth.login(request, userauth)  # 登录成功，db写sessionId
#             response = HttpResponseRedirect('/manage/')
#             # response.set_cookie("accountName", username, 10)  # 设置cookies
#             request.session["accountName"] = username  # 设置session
#
#             return response
#         else:
#             return render(request, 'login.html', {'msg': '账号或密码错误'})


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
