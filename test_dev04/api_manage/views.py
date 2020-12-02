import json
import requests
from django.http import JsonResponse
from project_manage.models import Project, Module


# Create your views here.

def req(request):
    if request.method == "POST":
        req_url = request.POST.get("reqURL", "")
        req_method = request.POST.get("reqMethod", "")
        req_type = request.POST.get("reqType", "")
        req_param = request.POST.get("reqParam", "")
        print(req_param)
        req_str = json.dumps(req_param)  # 处理json为字符串
        print(req_str)
        if req_url == "" or req_method == "" or req_type == "" or req_str == "":
            return JsonResponse({"code": 401, "msg": "False", "data": "请求参数为空"})
        # 判断选择的请求法法
        if req_method == "post":
            if req_type == "json":
                r = requests.post(req_url, json=req_str)
            elif req_type == "data":
                r = requests.post(req_url, data=req_str)
            else:
                return JsonResponse({"code": 403, "msg": "False", "data": "参数类型不支持"})
        elif req_method == "get":
            r = requests.get(req_url, params=req_str)
        else:
            return JsonResponse({"code": 404, "msg": "False", "data": "请求方法不支持"})
        return JsonResponse({"code": 200, "msg": "True", "data": r.text})
    else:
        return JsonResponse({"code": 402, "msg": "False", "data": "请求方法错误"})


def debug(request):
    return JsonResponse({"code": 200, "msg": "true", "data": "12312312312"})


def assertResult(request):
    if request.method == "POST":
        ac = request.POST.get("assertContent", "")
        ar = request.POST.get("assertResult", "")
        print("assertContent=>>>>>", ac)
        print("assertResult=>>>>>", ar)
        if ac == "" or ar == "":
            return JsonResponse({"code": 400, "msg": "False", "data": "结果或者断言内容为空！"})
        if ac in ar:
            return JsonResponse({"code": 200, "msg": "True", "data": "断言成功！"})
        else:
            return JsonResponse({"code": 200, "msg": "True", "data": "断言失败！"})
    else:
        return JsonResponse({"code": 402, "msg": "False", "data": "请求方法错误"})


def select_data(request):
    """
    获取项目/模块列表，用于select渲染
    :param request:
    :return:
    # 将所有的选项按照[
         {一级项目
           [
               {二级模块
               }
           ]
         }]
    """
    if request.method == "GET":
        return JsonResponse({"code": 402, "msg": "False", "data": "请求方法错误"})
    data_list = []
    project = Project.objects.all()
    for p in project:
        project_dict = {
            "id": p.id,
            "name": p.name,
            "moduleList": []
        }
        module = Module.objects.filter(project_id=p.id)  # 获取对应的模块数据
        print(module)
        for m in module:
            module_dict = {
                "id": m.id,
                "name": m.name
            }
            project_dict["moduleList"].append(module_dict)  # 联动选项添加到一级选项中

        data_list.append(project_dict)
    return JsonResponse({"code": 200, "msg": "True", "data": data_list})
