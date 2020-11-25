from django import forms
from .models import Project, Module


# class my_form(forms.Form):
#     project_name = forms.CharField(max_length=8, label="项目名称", error_messages={"required": "该字段不能为空!"})
#     project_describe = forms.CharField(label="项目描述", widget=forms.Textarea)
#     project_status = forms.BooleanField(label="是否有效", required=False, initial=True)

class project_form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']
        exclude = ['', 'create_time']


class module_form(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['project', 'name', 'describe']
        exclude = ['', 'create_time']
