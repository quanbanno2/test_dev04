from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from case_manage.models import TestCase
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required  # 限制未登录状态不能进入视图
def case_list(request):
    testcase = TestCase.objects.all()  # 获取数据库值
    accountName = request.session.get("accountName", "")  # 获取 session
    return render(request, "case/case_list.html", {"accountName": accountName, "caseDetail": testcase})


#
# @login_required  # 限制未登录状态不能进入视图
# def case_postman(request):
#     accountName = request.session.get("accountName", "")  # 获取 session
#
#     return render(request, "case/postman.html", {"accountName": accountName})


@login_required  # 限制未登录状态不能进入视图
def case_save(request):
    if request.method == "POST":
        req_url = request.POST.get("reqURL", "")
        req_method = request.POST.get("reqMethod", "")
        if req_method == "GET":
            req_method = 1
        elif req_method == "POST":
            req_method = 2
        req_type = request.POST.get("reqType", "")
        if req_type == "data":
            req_type = 1
        elif req_type == "json":
            req_type = 2
        req_param = request.POST.get("reqParam", "")
        assert_content = request.POST.get("assert_content", "")
        result = request.POST.get("result", "")
        module_id = request.POST.get("ModuleSelect", "")
        case_name = request.POST.get("caseName", "")
        if req_url == "" or req_method == "" or req_type == "" or req_param == "" or case_name == "":
            return JsonResponse({"code": 401, "msg": "False", "data": "请求参数为空"})

        TestCase.objects.create(name=case_name, url=req_url, method=req_method, request_type=req_type,
                                request_body=req_param, response=result, response_assert=assert_content,
                                module_id=module_id)

        return JsonResponse({"code": 200, "msg": "True", "data": "保存成功"})
    else:
        return JsonResponse({"code": 402, "msg": "False", "data": "请求方法错误"})


@login_required  # 限制未登录状态不能进入视图
def case_edit(request, cid):
    accountName = request.session.get("accountName", "")  # 获取 session

    return render(request, "case/case_edit.html", {"accountName": accountName})


@login_required  # 限制未登录状态不能进入视图
def case_edit_save(request):
    if request.method == "POST":
        req_url = request.POST.get("reqURL", "")
        req_method = request.POST.get("reqMethod", "")
        if req_method == "GET":
            req_method = 1
        elif req_method == "POST":
            req_method = 2
        req_type = request.POST.get("reqType", "")
        if req_type == "data":
            req_type = 1
        elif req_type == "json":
            req_type = 2
        req_param = request.POST.get("reqParam", "")
        assert_content = request.POST.get("assert_content", "")
        result = request.POST.get("result", "")
        module_id = request.POST.get("ModuleSelect", "")
        case_name = request.POST.get("caseName", "")
        case_id = request.POST.get("caseId", "")
        if req_url == "" or req_method == "" or req_type == "" or req_param == "" or case_name == "":
            return JsonResponse({"code": 401, "msg": "False", "data": "请求参数为空"})
        testcase = TestCase.objects.get(id=case_id)
        testcase.name = case_name
        testcase.method = req_method
        testcase.request_type = req_type
        testcase.request_body = req_param
        testcase.response = result
        testcase.response_assert = assert_content
        testcase.module_id = module_id
        testcase.save()
        return JsonResponse({"code": 200, "msg": "True", "data": "保存成功"})
    else:
        return JsonResponse({"code": 402, "msg": "False", "data": "请求方法错误"})


@login_required  # 限制未登录状态不能进入视图
def case_delete(request):
    if request.method == "POST":
        try:
            caseId = request.POST.get("caseId", "")
            TestCase.objects.filter(id=caseId).delete()
            return JsonResponse({"code": 10200, "msg": "True", "data": "删除成功"})
        except TestCase.DoesNotExist:
            return JsonResponse({"code": 10103, "msg": "True", "data": "用例不存在"})
