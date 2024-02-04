# import Task,並序列化Model裡的資料成為JSON
# 也可以將JSON反序列化回來Model
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # 將Task帶進來
        fields = "__all__"
        # 這邊我要序列化所有欄位
