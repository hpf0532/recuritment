from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Job(models.Model):
    JobTypes = [
        (0, "技术类"),
        (1, "产品类"),
        (2, "运营类"),
        (3, "设计类")
    ]
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name="职位类型")
    job_name = models.CharField(max_length=250, blank=False, verbose_name="职位名称")
    Cities = [
        (0, "北京"),
        (1, "上海"),
        (2, "深圳")
    ]
    job_city = models.SmallIntegerField(blank=False, choices=Cities, verbose_name="工作地点")
    job_reponsibility = models.TextField(max_length=1024, blank=False, verbose_name="职位职责")
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name="职位要求")
    creater = models.ForeignKey(User, verbose_name="创建人", null=True, on_delete=models.SET_NULL)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified_date = models.DateTimeField(auto_now=True, verbose_name="更新时间")