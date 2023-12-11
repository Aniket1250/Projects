from django.shortcuts import render,redirect 
# from django.http import HttpResponse 
from .models import Task 
# Create your views here. 


def home(request):
    context = {'success': False }
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        # ins =Task(taskTitle=title,taskDesc=desc)
        # ins.save()
        Task(taskTitle=title,taskDesc=desc).save()
        # success = True
        context = {'success': True }
    return render(request,'index.html',context)

def tasks(request):
    task=Task.objects.all()
    datas={'data':task}
    return render(request,'task.html',datas)

def delete(request,id):
    if request.method=="GET":
        data=Task.objects.get(taskid=id)
        # print(data.title)
        # dt={'data':'Successfully data is deleted'}
        data.delete()
        # return render(request,'delete.html',dt)
        return redirect ('/task')

def update(request,id):
    if request.method == 'GET':
        data=Task.objects.get(taskid=id)
        dt={'data':data}
        return render(request,'update.html',dt)
    
    if request.method == 'POST':
        data=Task.objects.get(taskid=id)

        title = request.POST.get('title')
        desc = request.POST.get('desc')
        complete='complete' in request.POST  

        data.taskTitle=title
        data.taskDesc=desc
        data.complete=complete
        data.save()
        return redirect('/task')
    

    # data =Task.objects.get(taskid=id)
    # dt = {'data': data}
    # if request.method == 'POST':
    #     title = request.POST.get('taskTitle')
    #     desc = request.POST.get('taskDesc')
    #     data.taskTitle = title
    #     data.taskDesc = desc
    #     data.save()
    # return render(request, 'update.html', dt)