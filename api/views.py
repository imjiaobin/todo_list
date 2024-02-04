from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "List": "/task-list/",
        "Detail View": "/task-datail/<str:pk>",
        "Create": "/task-create/",
        "Update": "/task-update/<str:pk>",
        "Delete": "/task-delete/<str:pk>",
    }
    return Response(api_urls)


@api_view(["GET"])
def taskList(request):
    tasks = Task.objects.all().order_by("-id")  # -id降冪排序
    serializer = TaskSerializer(tasks, many=True)
    # 將每一個tasks抓到的屬性序列化
    return Response(serializer.data)


@api_view(["GET"])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    # 這邊是要處理API,所以我們用request去抓data,而不是用HTTP方法
    # request.data回傳的是JSON

    if serializer.is_valid():
        serializer.save()
        # 回傳到db
    return Response(serializer.data)


@api_view(["POST"])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item successfully delete")


# apiOverview(request) 定義一個API的CRUD概述
# taskList(request) 使用TaskSerializer來將task物件序列化為JSON數據
# taskDetail(request, pk) 以pk參數從資料庫撈東西,回傳單一一個物件任務的訊息
# taskCreate(request) 使用TaskSerializer將傳入的資料反序列化為物件,以達到在資料庫創建新的任務
# taskUpdate(request, pk) 以pk抓到相應的物件,透過TaskSerializer來反序列化,以更新該pk的任務資訊
# taskDelete(request, pk) 和更新一樣的原理,只適用於刪除資料
# @app_view() 用來處理不同HTTP方法的裝飾器,可以以陣列的方式放入多個方法
