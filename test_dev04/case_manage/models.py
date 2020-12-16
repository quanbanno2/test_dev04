from django.db import models
from project_manage.models import Module


# Create your models here.

class TestCase(models.Model):
    """
    测试用例表
    """
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=50, null=False)
    url = models.TextField("URL", null=False)
    method = models.IntegerField("请求方法", null=False)  # 1:GET, 2: POST, 3:PUT, 4:DELETE
    request_type = models.IntegerField("参数类型", null=False)  # 1：form-data 2: json
    request_body = models.TextField("参数内容", null=False)
    response = models.TextField("请求响应", null=False)
    response_assert = models.TextField("断言内容", null=False)
    update_time = models.DateTimeField("更新时间", auto_now=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.name
