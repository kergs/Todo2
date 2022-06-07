from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from django.http import JsonResponse
# Create your views here.


@api_view(['GET'])
def todoOverview(request):
    api_urls= {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:id>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:id>/',
		'Delete':'/task-delete/<str:id>/',
		}
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, id):
	tasks = Task.objects.get(pk=id)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, id):
	task = Task.objects.get(pk=id)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, id):
	task = Task.objects.get(pk=id)
	task.delete()

	return Response('Item succsesfully delete!')

# Create your views here.
