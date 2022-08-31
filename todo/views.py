#url geldiginde fonksiyonu calistirir
from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from .models  import Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import productSerializer

# Create your views here.
def index(request):
    '''return HttpResponse('Anasayfa')
   context= {'num1' : 120,
              'numbers' :[1,2,3,4,5,6,7]}'''
    todos = Todo.objects.all()
    todos_reversed = todos[::-1]
    return render(request, 'index.html', {'todos_reversed': todos_reversed })

def addTodo (request):
    todos = Todo.objects.all()
    todos_reversed = todos[::-1]
    if request.method == "GET" :
        return redirect ('/')
    else:
        title = request.POST.get ('title')
        newTodo = Todo(title = title, completed = False)
        newTodo.save()
        return redirect ('/')

def update (requeest,id):
    #database e sorgu atiyoruz
    #todo =Todo.objects.filter (id = id).first()
    todo = get_object_or_404(Todo, id=id)

    todo.completed = not todo.completed

    todo.save()
    return redirect ('/')
def delete(request, id):
    todo = get_object_or_404(Todo,id=id)
    todo.delete()
    return redirect('/')



@api_view(['GET'])
def api(request):
    api_urls = {
    'List' :'/task_list/',
                }
    return Response (api_urls)

@api_view(['GET'])
def task_api(request):
    tasks = Todo.objects.all()
    serializer= productSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def task_create_api(request):
    serializer= productSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def task_update_api(request, pk ):
    task = Todo.objects.get(id = pk)
    serializer= productSerializer(instance=task, data= request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def task_delete_api(request, pk ):
    task = Todo.objects.get(id = pk)
    task.delete()
    return Response('Item deleted')

