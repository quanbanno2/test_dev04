from django.db import models


# Create your models here.


class Project(models.Model):
    name = models.CharField("项目名", max_length=8, blank=False, default="")
    describe = models.TextField("描述", default="", null=True)
    status = models.BooleanField("状态", default=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)  # auto_now 不需程序赋值，自动获取数据更新时间
    create_time = models.DateTimeField("创建时间", auto_now_add=True)  # auto_now_add 不需程序赋值，自动获取数据创建时间

    def __str__(self):
        return self.name


class Module(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=8, blank=False, default="")
    describe = models.TextField("描述", default="", null=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.name
